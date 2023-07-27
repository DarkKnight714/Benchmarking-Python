# For CPython
filename="5l.txt"
fopen=open(filename)
doc=[]
for line in fopen:
    x=line.split()
    doc.append(x)
doc.sort(reverse=True)
print(doc)


