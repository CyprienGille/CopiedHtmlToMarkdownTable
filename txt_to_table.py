#%%
from os import write
import sys

file_path = sys.argv[1]
num_cols = int(sys.argv[2])

with open(file_path) as f:
    lines = f.readlines()

out = "|"
header = True
col_id = 0
for line in lines:
    if col_id < num_cols:
        if line != "\n":
            out += line.replace("\n", "") + "|"
            col_id += 1
    else:
        # we reached the end of a line
        out += "\n|"
        # reset col index
        col_id = 0
        if header:  # last line was the header, we need the delim line
            out += "---|" * num_cols + "\n|"
        header = False

with open("output.txt", "w") as f:
    f.write(out)
