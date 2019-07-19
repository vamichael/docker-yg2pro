#!/usr/bin/env python3
from shutil import copyfile
import os


head = '.ignore.head';
git = head + '.git';
hg = head + '.hg';

body = 'ignore.body';
tmp = body + '.tmp';


if os.path.exists(tmp):
  os.remove(tmp)

f = open(body, 'r')
lines = f.readlines()
f.close()
count=len(lines);
lines.sort();

outFile = open(tmp, 'w');

for line in range(0, count):
    outFile.write("%s" % lines[line]);

outFile.close();

os.remove(body);
os.rename(tmp, body);

filenames = [git, body]
with open('.gitignore', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

filenames = [hg, body]
with open('.hgignore', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
