from os.path import abspath, isfile, join
from  glob import glob
import sys

print("Calculating...")

total = 0
totalFiles = 0

for f in [abspath(x) for x in glob(join("./", '*')) if isfile(x)]:
    if f.endswith("py"):
        file = open(f, "r")
        lineCount = len(file.readlines())
        print(file.name + " | " + str(lineCount))
        total += lineCount
        totalFiles+=1
        file.close()

print(str(total) + " Lines over " + str(totalFiles) + " files.")