1)
CREATE DOMAIN Age as INT
CHECK (value >= 10 And value <= 100);

CREATE DOMAIN sex as VARCHAR(1)
CHECK (value in('M', 'F'));

CREATE TABLE Cours
(
  id_cours INT PRIMARY KEY NOT NULL,
  Danse VARCHAR(10),
);

INSERT INTO Cours VALUES
(1, 'Salsa'),
(2, 'Salsa'),
(3, 'Rock'),
(4, 'Rock'),
(5, 'Rock'),
(6, 'Tango'),
(7, 'Tango');

CREATE TABLE Intervenant
(
  id_intervenant INT PRIMARY KEY NOT NULL,
  nomi VARCHAR(10),
);

INSERT INTO Intervenant VALUES
(1, 'Rey'),
(2, 'Gilles'),
(3, 'Denis'),
(4, 'Amandine');

CREATE TABLE Participant
(
  id_participant INT PRIMARY KEY NOT NULL,
  nomp VARCHAR(10),
  age Age,
  sexe sex
);

INSERT INTO Participant VALUES
(1, 'Roger', 30, 'M'),
(2, 'Melanie', 33, 'F'),
(3, 'Suzanne', 39, 'F'),
(4, 'Henri', 28, 'M');

CREATE TABLE inscription (
  id_cours INT REFERENCES Cours(id_cours),
  id_participant INT REFERENCES Participant(id_participant),
  PRIMARY KEY (id_cours, id_participant)
);

INSERT INTO Inscription VALUES
  (1, 1), (2, 2), (1, 4),
  (3, 4), (4, 3), (4, 2),
  (4, 1), (5, 4), (6, 4),
  (7, 3), (6, 2), (6, 1),
  (7, 4), (6, 3);

CREATE TABLE Atelier
(
  id_cours INT references Cours(id_cours),
  id_intervenant INT references Intervenant(id_intervenant),
  PRIMARY KEY (id_cours, id_intervenant)
);

INSERT INTO Atelier VALUES
  (1, 1), (1, 2), (2, 1),
  (3, 4), (4, 4), (4, 3),
  (5, 2), (6, 1), (7, 4),
  (7, 3);

INSERT INTO cours VALUES (5, 'valse');

INSERT INTO Atelier VALUES (1, 5);

DELETE FROM Cours WHERE id_cours = 1;

INSERT INTO Cours VALUES (8, 'slow'), (9, 'chachacha');

INSERT INTO Intervenant VALUES (8, 'Quentin');

INSERT INTO Atelier VALUES (9, 5);
