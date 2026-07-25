class Human:
    company="Tesla"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print("My name is:",self.name)
        print("My age is:",self.age)

    @staticmethod
    def addTwoNum(num1,num2):
        print("The sum is:",(num1+num2))

h1=Human("Pranvi",78)
h1.details()

h2=Human("Shiva",78)
h2.details()

# Human.addTwoNum(5,8)
# print(h1.company)
# h2.company="Hero"
# print(h2.company)

# print(dir(h1))
# print(h1.__dict__)
# help(str.upper)
# help(str.lower)