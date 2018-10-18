import sys
import CSVFile

bolsistas = CSVFile.CSVFile(sys.argv[1])

bolsistas.load()

ranks = bolsistas.getColumn(3, int)

top100 = 0
top1k = 0
top10k = 0

for rank in ranks:
	if rank <= 10000:
		top10k = top10k + 1

		if rank <= 1000:
			top1k = top1k + 1

			if rank <= 100:
				top100 = top100 + 1

print("Top 100: " + str(top100))
print("Top 1k: " +str(top1k))
print("Top 10k: " + str(top10k))