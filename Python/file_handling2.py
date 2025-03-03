file = open("mca.txt","r")
nlines = int (input("Enter The Number Of Line Which YOu Want To Read:"))
lines=file.readlines()
for i in range(nlines):
    print(lines[i])