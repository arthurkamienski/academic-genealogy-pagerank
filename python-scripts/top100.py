import sys
import CSVFile

def getTop(n, data):
	topn = []

	for i in range(0, n):
		topn.append(data[i])

	return topn

def sortBy(n, data):
	data.sort(key=lambda e: e[n], reverse=True)

file = CSVFile.CSVFile(sys.argv[1])
file.load()

data = file.getColumns([
	(0, str),
	(2, float),
	(4, float),
	(7, float),
	(9, str)])

areas = [
'Engenharias',
'Ciencias Da Saude',
'Linguistica Letras E Artes',
'Ciencias Humanas',
'Ciencias Biologicas',
'Ciencias Sociais Aplicadas',
'Ciencias Agrarias',
'Ciencias Exatas E Da Terra']

pesqs = []

for n in range(1, 4):
	sortBy(n, data)

	for pesq in getTop(1000, data):
		if not pesq in pesqs:
			pesqs.append(pesq)

with file.open(topPesqs.csv, 'w') as f:
	for pesq in pesqs:
		for n in range(0,4):
			f.print(str(pesq[n]) + ',')
		f.print(pesq[4])