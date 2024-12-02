sal=int(input("enter salary = "))
if sal<=500000:
    tax=0
elif (sal>500000 and sal<=750000):
    tax=0.1*(sal-500000)
elif (sal>750000 and sal<=1000000):
    tax=0.1*250000+0.2*(sal-750000)
else:
    tax=0.1*250000+0.2*250000+0.3*(sal-1000000) 
print(tax)
