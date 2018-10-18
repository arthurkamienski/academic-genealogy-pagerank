import sys

f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'r')

string1 = f.readline()
string2 = g.readline()

string1 = f.readline().rstrip().split(', ')
string2 = g.readline().rstrip().split(', ')

while string1 != [''] and string2 != [''] and float(string1[1]) == float(string1[1]):
	string1 = f.readline().rstrip().split(', ')
	string2 = g.readline().rstrip().split(', ')


if string1 != [''] or string2 != ['']:
	print('nao')
else:
	print('sim')