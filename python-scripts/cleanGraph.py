import sys

def isNumber(string):
	try:
		int(string)
		return True
	except:
		return False

def read(fileName):
	with open(fileName, 'r') as sourceFile, open('clean-' + fileName, 'w') as newFile:
		sourceFile.readline()
		newFile.write('Vertices> Numero, Nome\n')

		edges = False

		for line in sourceFile:
			field = line.split(',')

			if not edges:
				if isNumber(field[0]):
					if field[3] != '':
						newFile.write(field[0].strip() + ', ' + field[3].strip('"') + '\n')
				else:
					newFile.write('Arestas> Orientador, Orientando\n')
					edges = True
			else:
				newFile.write(field[0].strip() + ', ' + field[1].strip() + '\n')

read(sys.argv[1])