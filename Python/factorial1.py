try:
    fact = 1
    num = int (input("Enter The Number:"))
    assert num > 0
    for i in range(1, num+1):
        fact *=i
    print(fact)
except:
    print("Negative Number")