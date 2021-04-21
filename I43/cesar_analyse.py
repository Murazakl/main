import string


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


def cherche_cle_cesar(chaine):
    francais = [942, 102, 264, 339, 1587, 95, 104, 77, 841, 89, 0, 534,
                324, 715, 514, 286, 106, 646, 790, 726, 624, 215, 0, 30, 24, 32]
    corr = [0] * 26
    for dec in range(26):
        res = frequences(cesar(chaine, -dec))
        corr[dec] = sum(a * b for a, b in zip(res, francais))
    return corr.index(max(corr))


s = 'wldnpydpfcopxlcclezfedpfwlacpdbfpwlazcepdpdzteqpcxpptwopdnpyoltetwylccpeltealdopopdnpyocpaftdtwdlccpelpyqtywlazcepdzfgctepeolgtopfewldefapfcopdlgtpopglyewftdpopawzjltefynzxawpiptyqzcxletbfpfypgtyreltypopapcdzyypddpopawlnltpyeofyazdeplwlfecpcprlcolyelfalddlrpwpdpnclydrplyedxfclfidtefpdlfqzyoopwldlwwptwjlgltemtpyfypntybflyeltypozcotylepfcdntybpnclydrplyedpedtefppyecpwpdpnclydrplyedpewpdzcotylepfcdfypxlnstypctptxacpddtzyylyep'
print(cherche_cle_cesar(s))
