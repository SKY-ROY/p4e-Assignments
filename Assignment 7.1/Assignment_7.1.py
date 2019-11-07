# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fstring = fh.read()
fstring.strip()
print(fstring.upper())