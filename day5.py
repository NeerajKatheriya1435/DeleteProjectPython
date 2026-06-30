

# value=6

# match(value):
#     case 1|6|8|10:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case _:
#         print("Please input 1 to 4")

# value=57
# match(value):
#     # case 1|6|8|10:
#     #     print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     # case 4:
#     #     print("Wednesday")
#     case _ if value%2==0:
#         print("Even Number")
#     case _ if value%2==1:
#         print("Odd Number")

# inp1=int(input("Enter the num1: "))
# inp2=int(input("Enter the num2: "))
# opt=input("Enter the operator: ")

# match(opt):
#     case "+":
#         print("The sum is: ",(inp1+inp2))
#     case "-":
#         print("The sub is: ",(inp1-inp2))

# print(1)
# print(2)
# print(3)

# for i in range(11):
#     print(i)

# for i in range(5,21,2):
#     print(i)

# table=534
# for i in range(1,11):
#     print(i*table)

# i=1
# while(i<11):
#     print(i*table)
#     i+=1

# for i in range(11):
#     if(i==5):
#         break
#     print(i)

# for i in range(11):
#     if(i==5 or i==6):
#         continue
#     print(i)

# a=6
# b=3
# print(a+b)

# a1=7
# b1=9
# print(a1+b1)

def addTwoNum(num1,num2):
    # print(num1+num2)
    avg=(num1+num2)/2
    return avg

def subTwoNum(num1,num2):
    print(num1-num2)

def greet():
    print("Hello Morning")

# greet()
# greet()
# addTwoNum(4,7)
# addTwoNum(6,3)
# greet()
# subTwoNum(8,4)

print(addTwoNum(5,7))