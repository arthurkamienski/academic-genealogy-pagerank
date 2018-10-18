class CSVFile:
	def __init__(self, path = ''):
		self.setPath(path)
		self.setNLines(None)
		self.setLines([])
		self.setHeader(None)

	def load(self):
		with open(self.getPath(), 'r') as source:
			self.setHeader(source.readline().split(','))
			self.setLines([])
			self.setNLines(0)

			for line in source:
				self.setNLines(self.getNLines() + 1)
				self.getLines().append(line.split(','))

	def getColumn(self, number, convert=str):
		column = []

		for line in self.getLines():
			column.append(convert(line[number].strip()))

		return column

	def getColumns(self, numbers):
		columns = []

		for line in self.getLines():
			column = []
			for number, convert in numbers:
				column.append(convert(line[number].strip()))
			columns.append(column)

		return columns

	def removeColumn(self, number = None):
		if number != None:
			for line in self.getLines():
				line.pop(number)
		else:
			for line in self.getLines():
				line.pop()

		return columns

	def addColumn(self, newColumn, place = None):
		lines = self.getLines()

		if len(newColumn) == self.getNLines():
			if place == None:
				for i in range(self.getNLines()):
					lines[i].append(newColumn[i])
			else:
				for i in range(self.getNLines()):
					lines[i].insert(place, newColumn[i])
		else:
			print('Different sizes')

	def addLine(self, line):
		self.getLines().append(line)

	def saveFile(self, fileName):
		with open(fileName, 'w') as newFile:
			for line in self.getLines():
				for i in range(len(line)-1):
					newFile.write(line[i] + ', ')
				newFile.write(line[len(line)-1] + '\n')

	def getLines(self):
		return self.__lines

	def setLines(self, lines):
		self.__lines = lines

	def getNLines(self):
		return self.__nLines

	def setNLines(self, nLines):
		self.__nLines = nLines

	def getPath(self):
		return self.__path

	def setPath(self, path):
		self.__path = path

	def getHeader(self):
		return self.__header

	def setHeader(self, header):
		self.__header = header