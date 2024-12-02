# WE ARE LEARNING OOPS
class movie:
    x=10
    def __init__(self):
        movie.s=100
        self.a=10
    def m1(self):
        movie.u=800
        self.b=50
        self.z=50
        del movie.x
    @classmethod
    def cm(cls):
        cls.d=150
        del cls.u 
        
obj1=movie()
obj1.m1()
obj1.c=30
movie.cm()
print(movie.__dict__) 

