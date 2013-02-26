#!/usr/bin/python
with open("vita.md") as fp:
    lines = fp.readlines()

lines2 = lines[6:]

# print lines2

with open("vita_noyaml.md", "w") as fp:
    fp.writelines(lines2)