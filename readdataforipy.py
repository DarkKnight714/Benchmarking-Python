#for Iron Python
filename = "5l.txt"
with open(filename) as fopen:
    doc = [line.split() for line in fopen]

doc.sort(reverse=True)
print(doc)
