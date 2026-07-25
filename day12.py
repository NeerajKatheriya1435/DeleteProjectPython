class Human:

    def sleep(self):
        print("Human Can Sleep")
    def run(self):
        print("Human Can Run")

class Employee(Human):

    def canWork(self):
        print("Human Can Work")

class Programmer(Employee):

    def canProgram(self):
        print("Human Can Program")

# h1=Human()
# h1.sleep()
# h1.run()
# h1.canWork()

# h1=Employee()
# h1.sleep()
# h1.run()
# h1.canWork()
# h1.canProgram()

h1=Programmer()
h1.sleep()
h1.run()
h1.canWork()
h1.canProgram()