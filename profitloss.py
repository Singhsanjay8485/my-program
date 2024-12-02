cost_price=int(input("enter cost price = "))
selling_price=int(input("enter selling price = "))

if cost_price<selling_price:
    print("profit=",selling_price-cost_price)
elif selling_price<cost_price:
    print("loss=",cost_price-selling_price) 
else:
    print("no loss no profit=0")
       
    
