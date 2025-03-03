file = open("large.txt","r")
w = " "
for line in file:
    lines = line.split()
    for i in lines:
        if len(w)<len(i):
            w=i
print(w)