def alphabet(Message):
    li1 = ["âà", "éèêë", "îï", "ô", "ûü", "ç"]
    li2 = ["A", "E", "I", "O", "U", "C"]
    i = 0
    # Remplacement des caractères accentués éventuels
    for mot in li1:
        repl = li2[i]
        for lettre in mot:
            Message = Message.replace(lettre, repl)
        i += 1
    for lettre in "',-;:!?. ":  # Suppression de la ponctuation
        Message = Message.replace(lettre, "")
    return Message


Message = "lascenseurdemarratoutseulapresquelaportesesoitfermeeildescendaitilnarretaitpasdedescendrepuisilsarretaenfinlaportesouvritetdavideutlastupeurdesaviedevantluisedeployaituncomplexeinformatiqueunevingtainedepersonnessedeplacaientdunpostealautreregardantaupassagelesecransgeantsmurauxsituesaufonddelasalleilyavaitbienunecinquantainedordinateurscinqecransgeantsetsitueentrelesecransgeantsetlesordinateursunemachinerieimpressionnante"

cle = 11

alphabet = alphabet(Message)
lg = len(alphabet)
MessageCrypte = ""

for i in range(lg):
    if alphabet[i] == ' ':
        MessageCrypte += ' '
    else:
        asc = ord(alphabet[i])+cle
        MessageCrypte += chr(asc+26*((asc < 97)-(asc > 122)))

print(MessageCrypte)

MessageCrypte = "wldnpydpfcopxlcclezfedpfwlacpdbfpwlazcepdpdzteqpcxpptwopdnpyoltetwylccpeltealdopopdnpyocpaftdtwdlccpelpyqtywlazcepdzfgctepeolgtopfewldefapfcopdlgtpopglyewftdpopawzjltefynzxawpiptyqzcxletbfpfypgtyreltypopapcdzyypddpopawlnltpyeofyazdeplwlfecpcprlcolyelfalddlrpwpdpnclydrplyedxfclfidtefpdlfqzyoopwldlwwptwjlgltemtpyfypntybflyeltypozcotylepfcdntybpnclydrplyedpedtefppyecpwpdpnclydrplyedpewpdzcotylepfcdfypxlnstypctptxacpddtzyylyep"
lg = len(MessageCrypte)
MessageClair = ""
cle = 11

for i in range(lg):
    if MessageCrypte[i] == ' ':
        MessageClair += ' '
    else:
        asc = ord(MessageCrypte[i])-cle
        MessageClair += chr(asc+26*((asc < 97)-(asc > 122)))

print(MessageClair)
