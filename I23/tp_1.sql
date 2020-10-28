1)
Select nom, age
From participant;

2)
Select avg(age)
From participant;

3)
Select count(sexe) AS Homme, count(sexe) AS Femme
From participant
Where sexe='M';

4)
Select count(distinct danse) AS nbrdanse
From cours;

5)
Select DISTINCT id_cours
From cours Natural Join inscription;

6)
Select danse
From inscription Right Join cours
ON inscription.id_cours = cours.id_cours
Where inscription.id_participant is null;

7)
Select nom
From intervenant, atelier
Where intervenant.id_intervenant = atelier.id_intervenant
And id_cours Not In (
  Select id_cours
  From inscription);

8)
Select distinct nom
From participant Natural Join inscription Natural Join cours
Where danse IN ('Rock','Salsa');

9)
Select danse, count(id_intervenant)
From cours Natural Join atelier
Group By danse;

10)
Select id_cours, nom
From intervenant Natural Join atelier;

11)
Select id_participant, nom, age
From participant
Order By age desc
limit 1;

12)
Select danse, count(id_cours)
From inscription Natural Join cours
Group By cours.danse
Order By count(id_cours) desc
Limit 1;

13)
Select id_cours
From atelier
Group By id_cours
Having count(id_cours) = 1
Order By id_cours;

14)
Select id_cours
From atelier
Group By id_cours
Having count(id_cours) >= all(Select count(*) From atelier Group By id_cours);

15)
Select id_cours, count(id_participant)
From inscription
Group By id_cours;

16)
Select count(id_cours)
From atelier
where id_intervenant=(2);

17)
Select id_participant, nom
From participant Natural Join inscription Natural Join cours
Where danse = 'Salsa';

18)
Select id_participant, nom
From participant Natural Join inscription Natural Join cours
Group By id_participant
Having count(distinct danse) = 2;

19)
Select id_cours, danse
From intervenant Natural Join atelier Natural Join cours
Where nom ='Amandine';

20)
Select id_cours, count(id_participant) As Nbrparticipant
From intervenant Natural Join atelier Natural Join cours Natural Join inscription
Where nom ='Amandine'
Group By id_cours;

21)
Select id_cours, danse
From cours Natural Join inscription Natural Join participant
Where nom in ('Mélanie','Henri')
Group By id_cours
Having count(id_cours) = 2;

22)
SELECT participant.id_participant, participant.nom
FROM participant, intervenant, inscription, atelier
WHERE participant.id_participant = inscription.id_participant
AND inscription.id_cours = atelier.id_cours
AND intervenant.id_intervenant = atelier.id_intervenant
AND intervenant.nom = 'Denis';

23)
Select count(*) As Nbrparticipant
From participant, intervenant, inscription, atelier
Where participant.id_participant = inscription.id_participant
And inscription.id_cours = atelier.id_cours
And intervenant.id_intervenant = atelier.id_intervenant
And intervenant.nom in ('Denis','Amandine');

24)
Select cours.id_cours, danse
From cours
Group By id_cours
Having (
  Select count(participant.sexe)
  From inscription, participant
  Where cours.id_cours = inscription.id_cours
  And inscription.id_participant = participant.id_participant
  And participant.sexe = 'M')
> all (
  Select count(participant.sexe)
  FROM inscription, participant
  Where cours.id_cours = inscription.id_cours
  And inscription.id_participant = participant.id_participant
  And participant.sexe = 'F');
