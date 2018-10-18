import numpy as np
from scipy.stats.stats import pearsonr
import sys

f = open(sys.argv[1], 'r')

string = f.readline()
string = f.readline().rstrip().split(',')

t = []

x, y = [], []

while string != ['']:

	x = float(string[3])
	y = float(string[8])
	
	t.append((x, y))

	string = f.readline().rstrip().split(', ')

x,y = zip(*t)

s = list(t)
x, y = zip(*s)

print(min(x))
print(max(x))
print(min(y))
print(max(y))

print(pearsonr(x, y))