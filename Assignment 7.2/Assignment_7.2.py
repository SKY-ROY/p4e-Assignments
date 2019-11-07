# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    line = line.strip('X-DSPAM-Confidence: ')
    total = total + float(line)
    count = count + 1 
print("Average spam confidence:", total/count)