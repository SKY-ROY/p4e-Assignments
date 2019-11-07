name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
hourcount = dict()
hrcount = None
tmplst = list()

#block to iterate through file and separate out the hours
for line in fh:
    if not line.startswith('From '):
        continue
    lst = line.split()
    lst = lst[5].split(':')
    hourcount[lst[0]] = hourcount.get(lst[0],0) + 1

#block to make a list of (hours, frequency) tuple
for k,v in hourcount.items():
    tmplst.append((k,v))

#block to sort the list by hours i.e. key here
tmplst = sorted(tmplst)
for k,v in tmplst:
    print(k,v)