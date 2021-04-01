import csv
import sys


if __name__ == "__main__":
    print(sys.argv)

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-i":
            inLoc = sys.argv[i+1]
        if sys.argv[i] == "-o":
            outLoc = sys.argv[i+1]

    csv.register_dialect("tsv", delimiter="\t")

    with open(inLoc, 'r') as inFile, open(outLoc, 'w') as outFile:
        reader = csv.reader(inFile, delimiter="\t")
        writer = csv.writer(outFile, delimiter="\t")

        for row in reader:
            chr, start, stop = row[:3]
            start = int(start)
            stop = int(stop)

            the_rest = row[3:]

            while start != stop:
                writer.writerow([chr, str(start), str(start + 1)] + the_rest)
                start += 1


