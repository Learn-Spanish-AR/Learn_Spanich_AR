import csv
import os
from os import walk

_, _, filenames = next(walk('./converted/'))

print("completed walking path")

for i in range(0,len(filenames)):
    new = filenames[i].split(".")
    filenames[i] = new[0]
print(filenames[0])
filenames = set(filenames)

print("completed removing mime extension")

src_name = []
src_transcript = []

with open('validated.tsv', encoding='utf8') as csv_file:
    reader = csv.reader(csv_file, delimiter= '\t')
    next(reader)
    for row in reader:
        name = row[1].split(".")
        if name[0] in filenames:
            src_name.append(name[0])
            src_transcript.append(row[2])

print("completed storing filename and transcript")

with open('Cvalidated.tsv', 'w', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile, delimiter = '\t')
    for i in range(0,len(src_name)):
        writer.writerow([src_name[i]+'.wav', src_transcript[i]])
