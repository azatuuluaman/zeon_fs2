import os
import sys

args = sys.argv

if not len(args) < 2:
    exit(0)

dir_name = '.zeon_fs2'
dir_files = os.listdir(dir_name)

files = []

for file in dir_files:
    if os.path.isfile(file): files.append(file)

str_files = " ".join(files)
print('Files:', len(files))
print(str_files)
