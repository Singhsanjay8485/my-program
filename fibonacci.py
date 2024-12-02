# fabonacci series with third variable
# a,b=0,1
# n=int(input("enter the number the terms = "))

# for i in range(1,n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

# fabonacci series without third variable
a,b=0,1
n=int(input("enter the number the terms = "))

for i in range(1,n):
    print(a,end=" ")
    b=a+b
    a=b-a

    
    
    
