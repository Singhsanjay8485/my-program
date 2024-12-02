class myclass:
    def __init__(self,name):
        self.name=name
        print(f"object{self.name} is created")
    def __del__(self):
        print(f"object{self.name} is being destroyed") 
t1=myclass("example")
t2=t1
t3=t1

print("hello everyone")


