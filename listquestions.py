# how to take input of a list
n=int(input("enter the value = "))
list=[]
for i in range(0,n):
    val=int(input(f"enter the value at index [{i}]"))
    list.append(val)
print("you 've entered")
print(list)    