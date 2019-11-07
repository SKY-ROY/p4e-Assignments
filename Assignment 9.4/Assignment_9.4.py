name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
wordcount = dict()
bigcount = None
count = 0

#block to iterate through file and separate out the email ids
for line in fh:
    if not line.startswith('From '):
        continue
    lst = line.split()
    count = count + 1
    wordcount[lst[1]] = wordcount.get(lst[1],0) + 1

#block to find the email id with maximum frequency
for k,v in wordcount.items():
    if  bigcount is None or v > bigcount:
        bigcount = v
        bigword = k
    
print(bigword, bigcount)