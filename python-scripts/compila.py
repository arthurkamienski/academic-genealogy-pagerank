import sys

with open(sys.argv[1], 'r') as source, open(sys.argv[2], 'r') as source2, open('out.csv', 'w') as dest:
	line1 = source.readline()
	line2 = source2.readline().split(',')

	i = 0

	try:
		while line2 != '' and line1 != '':
			dest.write(line1.strip() + ', ' + line2[0].strip() + '\n')
			line1 = source.readline()
			line2 = source2.readline().split(',')
	except Exception as e:
		print(e)