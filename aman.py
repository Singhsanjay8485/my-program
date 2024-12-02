even = []
odd = []

num = int(input("enter last number"))
print("even number:")
for i in range(1,num+1):
    if i%2==0:
        even.append(i)

print(even)
print("odd number:")
for i in range(1,num+1):
    if i%2!=0:
        odd.append(i)

print(odd)
