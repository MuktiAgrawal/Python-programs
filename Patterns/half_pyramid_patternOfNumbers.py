def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(str(j+1)+" ",end="")
        print()
n=int(input("Enter no. of rows: "))
pattern(n)