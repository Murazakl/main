def arithmetic_arranger(L, answer=False):
    if len(L) > 5:
        return "Error: Too many problems."

    op = {'+': lambda pair : str(pair[0] + pair[1]), '-': lambda pair : str(pair[0] - pair[1])}

    haut = []
    bas = []
    lines = []
    answers = []
    L2 = []

    for i in L:
        separation = i.split()
        taille_max = len(max(separation, key=len))

        for j in separation[::2]:
            if not (j.isnumeric()):
                return "Error: Numbers must only contain digits."
        if separation[1] not in op:
            return "Error: Operator must be '+' or '-'."
        elif taille_max > 4:
            return "Error: Numbers cannot be more than four digits."

        taille_line = taille_max + 2
        line = '-' * taille_line
        up = separation[0].rjust(taille_line, ' ')
        down = f"{separation[1]}{' ' * (taille_line - len(separation[2]) - 1)}{separation[2]}"

        haut += [up]
        bas += [down]
        lines += [line]

        if answer:
            res = op[separation[1]]([int(k) for k in separation[::2]])
            answers += [f"{res.rjust(taille_line, ' ')}"]
        
    L2 = '\n'.join(['    '.join(l) for l in (haut, bas, lines)])

    if answers:
        L2 += '\n' + '    '.join(answers)
    
    return L2

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
