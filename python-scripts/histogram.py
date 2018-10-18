#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import CSVFile
import sys

file = CSVFile.CSVFile(sys.argv[1])
file.load()
data = file.getColumn(1, float)

plt.hist(data, 150, log=True, rwidth=0.8)

plt.xlabel('PageRank Invertido Global')
plt.ylabel(u'Frequência')

# plt.savefig('histogram ' + sys.argv[1].replace('.gdf','.png'))
plt.show()