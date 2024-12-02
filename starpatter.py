n=int(input("enter n="))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print("  ",end=" ") 
    for j in range (1,(2*i)):
        print(" *",end=" ")
    print()
for i in range(1,n):
    for k in range(1,i+1):
        print("  ",end=" ") 
    for j in range (1,(2*n)-(2*i)):
        print(" *",end=" ")
    print()                    