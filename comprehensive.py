# print a list of a 1 to 10
# list=[i for i in range(1,11)]
# print(list)

# store even numbers from 1 to 100
# list=[i for i in range(1,101) if i%2==0 ]
# print(list)

# how to print square in a list
# list=[i*i for i in range(1,11)]
# print(list)

# input values through user in list and print their sum
# n=int(input("enter the value = "))
# list=[]
# for i in range(0,n):
#     val=int(input(f"enter the value at index [{i}]"))
#     list.append(val)
# print("you 've entered")
# print(list)

# sum=0

# for i in range(0,n):
#     sum=sum+list[i]
# print(" your sum is",sum)    

# how to print odd and even numbers in a list
# n=int(input("enter the value = "))
# list=[]
# for i in range(0,n):
#     val=int(input(f"enter the value at index [{i}]"))
#     list.append(val)
# print("you 've entered")
# print(list)
# list_even=[]
# list_odd=[]
# for i in range(0,n):
#     if(list[i]%2==0):
#         list_even.append(list[i])
#     else:
#         list_odd.append(list[i])
# print(list_even)
# print(list_odd)  

# n=int(input("enter the value = "))
# list=[]
# for i in range(0,n):
#     val=int(input(f"enter the value at index [{i}]"))
#     list.append(val)
# print("you 're list")
# print(list)

# index=int(input("enter the index you want to update = "))
# value=int(input("enter the value  you want to update at a index = "))

# list[index]=value
# print("your are updated list ")
# print(list)

# n=int(input("enter the value = "))
# list=[]
# for i in range(0,n):
#     val=int(input(f"enter the value at index [{i}]"))
#     list.append(val)
# print("you 're list")
# print(list)

# index=int(input("enter the index you want to insert = "))
# value=int(input("enter the value  you want to insert at a index = "))
# list.append(0)
# print(list)
# for i in range(n,index,-1):
#     list[i]=list[i-1]

# list[index]=value

# print(list)

# how to find search value
# n=int(input("enter the value = "))
# list=[]
# for i in range(0,n):
#     val=int(input(f"enter the value at index [{i}]"))
#     list.append(val)
# print("you 're list")
# print(list)
# index=int(input("enter the index you want to search = "))
# print("your search value is = ",end=" ")
# for i in range(0,n):
#     if(index>=0 and index<n):
#         if(i==index):
#              print(list[index])


n=int(input("enter the value = "))
list=[]
for i in range(0,n):
    val=int(input(f"enter the value at index [{i}]"))
    list.append(val)
print("you 're list")
print(list)
index=int(input("enter the index you want delete = "))
list.append(0)

for i in range(index,n):
    list[i]=list[i+1]

list=list[:n-1]

print(list)


        

        


