import sys

with open(sys.argv[1], 'r') as bolsistas:
	rank = [0, 0, 0, 0, 0, 0]
	
	bolsistas.readline()

	for bolsista in bolsistas:
		fields = bolsista.split(', ')

		for i in range(2, 8):
			rank[i-2] = rank[i-2] + float(fields[i])

	print(rank)