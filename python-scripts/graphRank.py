import sys
import matplotlib.pyplot as plt
import CSVFile
from collections import defaultdict

def contaRank(todos, codes, k):
	ranks = {}

	for code, rank in todos.getColumns([(0, int), (k, int)]):
		total, bolsistas = ranks.get(rank, [0, 0])
		total = total + 1

		if code in codes:
			bolsistas = bolsistas + 1

		ranks[rank] = [total, bolsistas]

	tups = []

	for rank in ranks:
		tups.append([rank, ranks[rank][0], ranks[rank][1]])

	tups = sorted(tups, key = lambda tup: tup[0])

	maximo = max(tups, key = lambda tup: tup[0])[0]

	totbols = len(codes)

	lists = {
	'RANK'         : [],
	'TOTALPESQS'   : [],
	'BOLS'         : [],
	'PERCENTPESQS' : [],
	'PERCENTRANK'  : []
	}

	tot = 0
	bols = 0

	for tup in tups:
		tup[1] = tup[1] + tot
		tup[2] = tup[2] + bols
		tot = tup[1]
		bols = tup[2]

	for r, t, b in tups:	
		lists['RANK'].append(float(r))
		lists['TOTALPESQS'].append(t)
		lists['BOLS'].append(b/totbols)
		lists['PERCENTPESQS'].append(float(b/t))
		lists['PERCENTRANK'].append(float(r)/maximo)

	return lists

def getNiveis(listaBolsistas):
	niveis = {
	'SR': [],
	'1A': [],
	'1B': [],
	'1C': [],
	'1D': [],
	'2' : []
	}

	for bolsista, nivel in listaBolsistas:
		niveis[nivel].append(bolsista)

	return niveis

	
todos = CSVFile.CSVFile(sys.argv[1])
bolsistas = CSVFile.CSVFile(sys.argv[2])

todos.load()
bolsistas.load()

listaBolsistas = bolsistas.getColumns([(2,int), (4,str)])

niveis = getNiveis(listaBolsistas)

n1 = niveis['1A'] + niveis['1B'] + niveis['1C'] + niveis['1D']
codes = n1 + niveis['SR'] + niveis['2']

codes = set(codes)

PR   = contaRank(todos, codes, 2)
# PRL1 = contaRank(todos, codes, 3)
# PRL2 = contaRank(todos, codes, 4)
PRL3 = contaRank(todos, codes, 5)
# PRL4 = contaRank(todos, codes, 6)
# PRL5 = contaRank(todos, codes, 7)
InD  = contaRank(todos, codes, 8)

plt.plot(  PR['PERCENTRANK'], PR  ['BOLS'], label='PageRank Global')
# plt.plot(PRL1['PERCENTRANK'], PRL1['BOLS'], label='PageRank Local k=1')
# plt.plot(PRL2['PERCENTRANK'], PRL2['BOLS'], label='PageRank Local k=2')
plt.plot(PRL3['PERCENTRANK'], PRL3['BOLS'], label='PageRank Local k=3')
# plt.plot(PRL4['PERCENTRANK'], PRL4['BOLS'], label='PageRank Local k=4')
# plt.plot(PRL5['PERCENTRANK'], PRL5['BOLS'], label='PageRank Local k=5')
plt.plot( InD['PERCENTRANK'], InD ['BOLS'], label='Out Degree')

# NUM = 2

# pr = contaRank(todos, set(niveis['2']), NUM)
# plt.plot(pr['RANK'], pr['BOLS'], label='Nível 2')

# pr = contaRank(todos, set(n1), NUM)
# plt.plot(pr['RANK'], pr['BOLS'], label='Nível 1')

# pr = contaRank(todos, set(niveis['SR']), NUM)
# plt.plot(pr['RANK'], pr['BOLS'], label='Nível Sênior')

plt.ylabel('Número de Bolsistas')
plt.xlabel('% do Rank')

plt.legend()

plt.show()