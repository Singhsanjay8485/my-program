n=int(input("enter number = "))
s=set()
for i in range(n):
    p=set(input(f"enter values for set{i+1} (separated by spaces):").split())
    s.update(p)
for i in range(n):
    x=set(int(input(f"enter values for set{i+1} (separated by spaces):").split()))
    s.update(x)



print("all unique values entered:")
for value in s:
    print(value) 
print(s)       