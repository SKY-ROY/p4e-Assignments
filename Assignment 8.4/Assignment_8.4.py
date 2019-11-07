fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lst1 = line.split()
    for words in lst1:
        if words in lst:
            continue
        lst.append(words)
lst.sort()
print(lst)