#!/usr/bin/python
with open("vita.md") as fp:
    lines = fp.readlines()

lines2 = lines[6:]
lines3 = lines[8:]

# print lines2
with open("vita_noyaml.md", "w") as fp:
    fp.writelines(lines2)

# print lines3
with open("vita_noyaml_nocvaspdf.md", "w") as fp:
    fp.writelines(lines3)


# onepage

with open("vita_onepage.md") as fp:
    lines = fp.readlines()

lines2 = lines[2:]
# lines3 = lines[8:]

# print lines2
with open("vita_onepage_noyaml.md", "w") as fp:
    fp.writelines(lines2)