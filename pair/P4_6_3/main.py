import re
strs = "foo\tbar\t\tspam"
re.split(r'\t+', strs)

with open('test.txt') as file:
    for line in file:
        line  =list(re.split(r'\t+',line))
        print(line)