import sys

f = open(sys.argv[1], 'r')
file = open(sys.argv[1].replace('.csv', '-norm.csv'), 'w')

s = f.readline()
file.write(s)

s = f.readline().rstrip().split(', ')

t = []

while s != ['']:
	x = float(s[1])
	y = float(s[2])

	t.append((s[0], x, y))

	s = f.readline().rstrip().split(', ')

maxPRs = {}

for p in t:
	maxPRs[p[2]] = max(maxPRs.get(p[2], 0), p[1])

for p in t:
	string = p[0] + ', ' + str(p[1]/maxPRs[p[2]]-p[1]) + ', ' + str(p[2]) + '\n'
	file.write(string)

file.close()