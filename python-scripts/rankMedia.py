import sys
import CSVFile
from operator import itemgetter as getter

def calculateRank(todos, codes):
	for pesq in todos:
		

todos = CSVFile.CSVFile(sys.argv[1])
bolsistas = CSVFile.CSVFile(sys.argv[2])

todos.load()
bolsistas.load()

codes = bolsistas.getColumn(1, int)

todosRankeados = CSVFile.CSVFile()