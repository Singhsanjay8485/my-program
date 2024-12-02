# has a relationship

class car:
    def __init__(self,cname,ccolor,cprice):
        self.cname=cname
        self.ccolor=ccolor
        self.cprice=cprice

    def printcardetails(self):
        print(f'car name is {self.cname}')
        print(f'car color is {self.ccolor}')
        print(f'car price is {self.cprice}')

class employee:
    def __init__(self,ename,eid,eaddress):
        self.ename=ename
        self.eid=eid
        self.eaddress=eaddress
        self.c=car('thar','black',1500000)#object creation of a car class

    def printempdetails(self):
        print()    
        

