try:
    fact =1
    num = int (input("Enter The Number:"))
    if num<0:
        raise Exception ("Negative Number")
    else:
        for i in range(1, num+1):
            fact *=i
        print(fact)
except Exception as e:
    print(e)