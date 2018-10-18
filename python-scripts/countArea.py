import sys

file = open(sys.argv[1], 'r')

string = file.readline().rstrip().split(', ')
string = file.readline().rstrip().split(', ')

l = []

while string != ['']:
	if string[2] not in l:
		l.append(string[2])
	string = file.readline().rstrip().split(', ')
c = 0

for s in l:
	c = c+1
	print str(c) + ' ' + s