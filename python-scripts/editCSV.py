import sys

def edit(source_file_name, columns, new_file_name):
	print('\nReading source file...')

	with open(source_file_name, 'r') as source_file:
		print('Creating new file named \"' + new_file_name + '\" with columns ' + str(columns) + '...')
		with open(new_file_name, 'w') as new_file:
			line_number = 0
			for line in source_file:
				line_number = line_number + 1

				fields = line.split(',')

				for column in columns:
					try:
						new_file.write(fields[column].strip())
					except IndexError:
						print('Line \"' + line + '\" (' + str(line_number) + ') does not have enough columns')

					if columns.index(column) < len(columns)-1:
						new_file.write(', ')
				new_file.write('\n')

	print('Done!')

def analise(file):
	with open(file, 'r') as file:
		#has_header = input('Is the first line of the file a header?\n').upper() in ['Y', 'YES', 'S', 'SIM']

		#if has_header:
		#	print("Interpreting the first line as a header.\n")
		#else:
		#	print("Interpreting the first line as data.\n")
		
		fields = file.readline().split(',')

		print(str(len(fields)) + ' fields found.')

		for field in fields:
			print(str(fields.index(field)) + " - " + field.strip())

		remove = input('What is the new order? (field numbers separated by spaces)\n')

		try:
			remove = [int(number) for number in remove.split(' ')]
		except ValueError:
			print('Invalid column numbers.')

		not_present = [number for number in remove if number > len(fields)-1 or number < 0]

		if len(not_present) == 0:
			print('\nNew column order: ' + str(remove) + '.')
			edit(sys.argv[1], remove, sys.argv[1] + ' clean')
		else:
			print('Invalid column numbers.')

analise(sys.argv[1])