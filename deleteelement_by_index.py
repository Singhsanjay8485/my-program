size=int(input("enter the value = "))
list=[]
for i in range(0,size):
    val=int(input(f"enter the value at index [{i}]"))
    list.append(val)
print("you 're list")
print(list)
index=int(input("enter the index you want delete = "))
list.append(0)
for i in range(index,size):
    list[i]=list[i+1]
list=list[:size-1]
print(list)
