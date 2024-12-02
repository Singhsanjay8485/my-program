class myclass:
    def instance_method(self):
        return "this is an instance method"
    @staticmethod
    def static_method():
        return "this is a static method"
    @classmethod
    def class_method(cls):
        return "this is a class method"    



obj=myclass()
print(obj.instance_method())        
print(myclass.static_method())
print(myclass.class_method())