import sys
import CSVFile

file = CSVFile.CSVFile(sys.argv[1])

file.load()

data = file.getColumn(int(sys.argv[2]), float)

print('Maximo: ' + str(max(data)))
print('Minimo: ' + str(min(data)))