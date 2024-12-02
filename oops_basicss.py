class test:
    a=5#static variable
    def m1(self):
        self.a=100#instance variable 
obj=test()
obj.m1()
print(test.__dict__)        

# class test:
#     a=5 
#     def __init__(self):#constructor
#         test.b=20
#         print(test.b)
#         print(self.b)
#     def m1(self):# instance method
#         test.c=30
#     @classmethod #
#     def class_method(cls):#class method
#         cls.d=40    
# obj=test()
# obj.m1()
# obj.class_method()
# print(test.__dict__)        

# class test:
#     a=5
#     def m1(self,p):
#         test.b=10
#         test.p=20
# obj=test()
# obj.m1(50)
# print(test.__dict__)        