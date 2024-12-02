class student:
    def setname(self,name):
        self.name=name
    def setgf(self,gname):
        self.gname=gname

    def getname(self):
        return self.name
    def getgname(self):
        return self.gname

n=int(input("enter the number of students"))
for i in range(n):
    s=student()
    name=input("enter name = ")
    s.setname(name)*/-*
    gf=input("enter gf name = ")
    s.setgf(gf)
    print(s.getname())
    print("loves")
    print(s.getgname())