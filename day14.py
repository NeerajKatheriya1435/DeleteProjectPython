class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def getName(self):
        return self.name
    
    @getName.setter
    def setName(self,other):
        if(not str(other).isnumeric()):
            self.name=other
           
    

h1=Human("Rohan",89)
print(h1.getName)

h1.setName="Shivam"
print(h1.getName)
# h1.name="Pranvi"
# h1.age=67
# h1.name=67
# h1.age="Rohan"

# print(h1.name)
# print(h1.age)