class movie:
    """THIS IS OUR CLASS ATTRIBUTES"""
    def __init__(self):
        self.name="dhadak"
        self.budget="150 cr"
        self.revenue="100 cr"
    def m1(self):
        self.year=2024
    def dl(self):
        del self.name
obj1=movie()
obj1.m1()
obj2=movie()
obj2.m1()
#obj1.dl()
#del obj1.name
#print(movie.__dict__)
print(obj1.__dict__)
print(movie.__doc__)
print(obj1.name)

