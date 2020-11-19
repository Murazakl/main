def minimum_posi(L): 
	pos = [0]
	mini = L[0]
	i = 1
	while i < len(L):
		if L[i] < mini:
			mini = L[i]
			pos = [i]
		elif L[i] == mini:
			pos.append(i)
		i += 1
	return pos

print(minimum_posi([3,2,5,7,2]))