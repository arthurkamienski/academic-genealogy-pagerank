import sys

file = open(sys.argv[1], 'r')

string = file.readline().rstrip().split(', ')
string = file.readline().rstrip().split(', ')
d = {}

while string != ['']:
	num = int(string[3])
	area = string[2]
	if num not in d:
		d[num] = {}

	if area not in d[num]:
			d[num][area] = 0

	d[num][area] = d[num][area] + 1
	string = file.readline().rstrip().split(', ')

for key in sorted(d.iterkeys()):
	print 'Geracao ' + str(key)
	print d[key]