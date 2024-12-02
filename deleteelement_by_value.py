size=int(input("enter the value = "))
list=[]
for i in range(0,size):
    val=int(input(f"enter the value at index [{i}]"))
    list.append(val)
print("you 're list")
print(list)
value=int(input("enter the value you want delete = "))
list=[x for x in list if x!=value]0
print(list)