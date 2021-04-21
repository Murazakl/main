import string

# PROBLEME A RESOUDRE : NE MARCHE QUE SI LE MESSAGE CRYPTE EST EN MAJUSCULE


def cesar(chaine, dec):
    alph = string.ascii_uppercase
    s = chaine.upper()
    return s.translate(str.maketrans(alph, alph[dec:] + alph[:dec]))


def frequences(chaine):
    freq = [0] * 26
    for c in chaine:
        if c in string.ascii_uppercase:
            freq[ord(c) - ord('A')] += 1
    somme = sum(freq)
    freq = [v / somme * 1000.0 for v in freq]
    return freq


def cle_cesar(chaine):
    francais = [942, 102, 264, 339, 1587, 95, 104, 77, 841, 89, 0, 534,
                324, 715, 514, 286, 106, 646, 790, 726, 624, 215, 0, 30, 24, 32]
    corr = [0] * 26
    for dec in range(26):
        res = frequences(cesar(chaine, -dec))
        corr[dec] = sum(a * b for a, b in zip(res, francais))
    return corr.index(max(corr))


def indice_coincidence(chaine):
    app = apparitions(chaine)
    s = sum(n * (n - 1) for n in app)
    somme = sum(app)
    return s / (somme * (somme - 1))


def apparitions(chaine):
    app = [0] * 26
    for c in chaine:
        if c in string.ascii_uppercase:
            app[ord(c) - ord('A')] += 1
    return app


def liste_indices(chaine, n):
    res = [0]
    for i in range(1, n + 1):
        res.append(sum(indice_coincidence(chaine[k::i]) for k in range(i)))
        res[-1] /= i
    return res


def longueur_cle(chaine, seuil=0.068, nmax=12):
    p = [(lcle, i) for lcle, i in enumerate(
        liste_indices(chaine, nmax)) if i > seuil]
    return p[0]


def cle_vigenere(chaine, n):
    return "".join(chr(ord('A') + cle_cesar(chaine[i::n])) for i in range(n))


u = "YIBMQEMEDBJYFEJWZWOVYSIWLCOPNZRMOMTXRRUYGMVVRRFQATUVRRTIDTKXNMKHZDKRHFCEIKARVRJXVVZMYECPVQZTRYKIOZKTRVUVZNRSEIEGZIBEAXDIHMJIYYZEQWOVNZFYZAURNQFYMQRHRZRMOMSTRGYIMXXIYYUIYMISAXZRPMXHNRJWJVJIYMIIHIOWPSDQZVZTBYMEDBOPFXFTKMXGRTRVVAOXRGIIZXGVYYZUPMRUHIJEIVKIFELTVZGZNRKGZVKXNMKTVAARNHMIMAGMEIFVYQTEVVVHVDOHNZRMOLKNNHVXMCOXCPLWYCTZVVLWHIOWVPJEBQYWNMKHZDOVHWZRNBGPYIJWPZJIFQRGCQTIFMJSGMKWNYASPZJLHMTINBARRWFVOMJIIMIYNYAMNTIMNXREPIJYMBUYFPVWJZJMAEKIPZYHRPRTGITIGIVXZVVPHWTIQQXYFRFQHMVVRPLHZIBEVXLRNWATPSERJVTITPZKZIHPRHZROMRPVKVRXM"
p = longueur_cle(u)
r, i = p
print(p)
print(cle_vigenere(u, r))


def dechiffre_vigenere(s, cle):
    l = []
    for i, c in enumerate(s):
        if c in string.ascii_uppercase:
            c = ord(c) - ord(cle[i % len(cle)])
            c = chr(c % 26 + ord('a'))
        l.append(c)
    return "".join(l)


print(dechiffre_vigenere(u, cle_vigenere(u, r)))
