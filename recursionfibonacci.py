def fibonacci(n):
    #'print fibonacci series using recursion'
    if(n<=0):
        return "input should be positive integer"
    'hello fibbonacci'    
    if n==1:
        return 0
    elif n==2:
        return 1 
    else:
        return fibonacci(n-1)+fibonacci(n-2)               

for i in range(1,10):
    print(fibonacci(i))
#'print fibonacci series using recursion'
print(fibonacci.__doc__)    

#'sum of a numbers'



# """my name is sanjay singh i am student of a wcsc 
# hello my name is rohan"""
# print(__doc__)