import sys
from operator import itemgetter as getter

def sortAndRank(pesqs, bols, k, rev=True):
	l = []

	for pesq in pesqs:
		l.append(pesq[k])

	l = sorted(l,reverse=rev)

	rank = {}

	r = 1
	rank[l[0]] = r

	for i in range(1, len(l)):
		if l[i] != l[i-1]:
			r = r + 1
		rank[l[i]] = r

	for pesq in pesqs:
		pesq.append(rank[pesq[k]])

with open(sys.argv[1], 'r') as pageranks, open(sys.argv[2], 'r') as bolsistas:
	pesqs = []
	bols = []
	p = {}

	pageranks.readline()
	bolsistas.readline()

	for line in pageranks:
		chunks = line.split(', ')

		pesq = []

		pesq.append(chunks[0])
		pesq.append(chunks[1])

		for chunk in chunks[2:9]:
			pesq.append(float(chunk))

		pesqs.append(pesq)
		p[pesq[1]] = pesq

	for line in bolsistas:
		chunks = line.split(',')
		bols.append(chunks[2].strip())

	for i in range(2, 9):
		sortAndRank(pesqs, bols, i)

	with open('Acacia-PageRanks-Rankeados.csv', 'w') as out:
		out.write('Nome, idLattes, Rank PR, Rank PR k=1, Rank PR k=2, Rank PR k=3, Rank PR k=4, Rank PR k=5, OutDegree\n')

		for pesq in pesqs:
			out.write(str(pesq[1]) + ', ')
			out.write(str(pesq[0]) + ', ')
			out.write(str(pesq[9]) + ', ')
			out.write(str(pesq[10]) + ', ')
			out.write(str(pesq[11]) + ', ')
			out.write(str(pesq[12]) + ', ')
			out.write(str(pesq[13]) + ', ')
			out.write(str(pesq[14]) + ', ')
			out.write(str(pesq[15]) + '\n')

	with open('Bolsistas-Rankeados.csv', 'w') as out:
		out.write('Nome, idLattes, Rank PR, Rank PR k=1, Rank PR k=2, Rank PR k=3, Rank PR k=4, Rank PR k=5, OutDegree\n')
		for bol in bols:
			if bol in p:
				out.write(str(p[bol][1]) + ', ')
				out.write(str(p[bol][0]) + ', ')
				out.write(str(p[bol][9]) + ', ')
				out.write(str(p[bol][10]) + ', ')
				out.write(str(p[bol][11]) + ', ')
				out.write(str(p[bol][12]) + ', ')
				out.write(str(p[bol][13]) + ', ')
				out.write(str(p[bol][14]) + ', ')
				out.write(str(p[bol][15]) + '\n')