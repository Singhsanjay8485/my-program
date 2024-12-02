n=int(input("enter your number = "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print("  ",end=" ")
    for k in range(1,2*i):
        print(" *",end=" ")
    print()    
for i in range(1,n):
    for j in range(1,i+1):
        print("  ",end=" ")
    for k in range(1,2*(n-i)):
        print(" *",end=" ")
    print()    

            