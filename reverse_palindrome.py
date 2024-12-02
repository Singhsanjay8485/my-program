n=int(input("your number n = "))
reversed=0
original=n

while(n!=0):
    remainder=n%10
    reversed=reversed*10+remainder
    n=n//10
print(reversed)   

if(original==reversed):
    print("number is palindrome")
else:
    print("number is not palindrome")    
for i in range(0,1):
    