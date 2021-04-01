import csv
from repeater import expandToList
from tqdm import tqdm


if __name__ == "__main__":

    test_file_name = "IP24.sorted.bed"
    test_out = "testout.bed"

    csv.register_dialect("tsv", delimiter="\t")

    with open(test_file_name, 'r') as inFile, open(test_out, 'w') as outFile:
        reader = csv.reader(inFile, delimiter="\t")
        writer = csv.writer(outFile, delimiter="\t")
        out = []

        for row in tqdm(reader):
            chr, start, stop = row[:3]
            start = int(start)
            stop = int(stop)

            the_rest = row[3:]

            while start != stop:
                writer.writerow([chr, str(start), str(start + 1)] + the_rest)
                start += 1


