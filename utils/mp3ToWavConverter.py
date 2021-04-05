import os
from os import path
from pydub import AudioSegment
import csv


src_name = []
src_path = './clips/'
dest_path = './converted/'

print(os.getcwd())

with open('validated.tsv', encoding='utf8') as csv_file:
    reader = csv.reader(csv_file, delimiter= '\t')
    next(reader)
    for row in reader:
        name = row[1].split(".")
        src_name.append(name[0])

for name in src_name:
    f = src_path+name+'.mp3'
    print(path.isfile(f))
    print(f)
    sound = AudioSegment.from_mp3(f)
    r = dest_path+name+'.wav'
    print(r)
    sound.export(r, format="wav")
