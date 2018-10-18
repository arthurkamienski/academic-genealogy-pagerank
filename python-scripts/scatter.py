import matplotlib.pyplot as plt
import numpy as np
import CSVFile
import sys

file = CSVFile.CSVFile(sys.argv[1])
file.load()

x = file.getColumn(1, float)
y = file.getColumn(2, float)

plt.scatter(x, y)

plt.axis([min(x) - 0.1*max(x), max(x) + 0.1*max(x), min(y) - 0.1*max(y), max(y) + 0.1*max(y)])

plt.xlabel('PageRank')
plt.ylabel('Tamanho')

# plt.savefig('scatter ' + sys.argv[1].replace('.gdf','.png'))
plt.show()
