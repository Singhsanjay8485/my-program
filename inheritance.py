#single level inheritance
# class parents:
#     def property(self):
#         print("property")
#     def bank(self):
#         print("bank balance")

# class child(parents):
#     def enjoy(self):
#         print("i am enjoying")        

# obj=child()
# obj.property()
# obj.bank()

# multilevel inheritance in python
# class parents:
#     def m1(self):
#         print("parent class")
# class c(parents):
#     def m2(self):
#         print("child class")
# class c2(c):
#     def m3(self):
#         print("sub child class")

# obj=c2()
# obj.m1()
# obj.m2()

# hierarchical inheritance

# class p:
#     def m1(self):
#         print("parent class")
# class c1(p):
#     def m2(self):
#         self.b=20
#         print("child 1 class")
# class c2(p):
#     def m3(self):
#         self.a=10
#         print("child 2 class")                

# obj1=c1()
# obj1.m1()
# obj1.m2()
# obj2=c2()
# obj2.m3()
# obj2.m1()
# print(obj2.__dict__)
# print(obj1.__dict__)


# multiple inheritance
class p1:
    def m1(self):
        print("parent1 class")
class p2:
    def m1(self):
        print("parent2 class")
class c(p2,p1):
    def m3(self):
        print("child class")
obj=c()
obj.m1()
obj.m1()
obj.m3()  
print(c.__mro__)                      