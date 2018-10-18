import sys

f = open(sys.argv[1], 'r')

string = f.readline()
string = f.readline().rstrip().split(', ')

t = []

while string != ['']:
	x = float(string[1])
	y = float(string[2])
	
	t.append((x, y))

	string = f.readline().rstrip().split(', ')

x, y = zip(*t)

print(len(x))
print(len(list(set(x))))
print(len(list(set(y))))

t = list(set(t))

x, y = zip(*t)

print(len(x))