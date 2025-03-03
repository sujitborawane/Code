file = open("mca.txt","r")
count = 0
for line in file:
    lines = line.split()
    for i in lines:
        count = count + 1          
print(count)