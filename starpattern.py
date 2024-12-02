# n=int(input("enter number = "))
# for i in range(0,n):
#     for k in range(0,i+1):
#         print("*" ,end=" ")
#     print()

# n=int(input("enter number n = "))
# for i in range(1,n+1):
#     for k in range(1,i+1):
#          print(k,end=" ")
#     print()
#with third variable
a=1
# n=int(input("enter number n = "))
# for i in range(1,n+1):
#     for k in range(1,i+1):
#          print(a,end=" ")
#          a = a+1
#     print()
# a=5  
# n=int(input("enter the number n="))
# for i in range(1,n+1):
#      for k in range(1,i+1):
#          print(a,end=" ")
#      a=a-1   
         
#      print()


n=int(input("enter the number n="))
for i in range(1,n+1):
    for k in range(n,i,-1):
         print(' ',end=" ")
    for j in range(0,i):
        print('*',end=" ")     
    print()
    