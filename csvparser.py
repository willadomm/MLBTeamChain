import csv


seen = []
dupes = []
f = open('names.txt', 'w')
d = open('dupes.txt', 'w')

with open("biofile0.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        stringname = row[2] + " " + row [1]
        print(stringname, file=f)

with open("names.txt") as n:
    for line in n:
        abbrline = line[:-1]
        if abbrline in seen:
            seen.append(abbrline)
            dupes.append(abbrline)
        else:
            seen.append(abbrline)

for name in dupes:
    print(name, file=d)
