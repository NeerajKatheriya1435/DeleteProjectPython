# s1=(3,41,5,6)
# print(s1)

# s1={3,41,5,6,3,7,6,6,4}
# print(s1)
# print(type(s1))

# s1={3,41,5,6}
# s1.add(89)
# s1.remove(6)
# s1.discard(6)
# s1.pop()
# s1.clear()
# print(s1)

# s1={4,7,9,2}
# s2={4,9,8,2}

# {4,7,9,2,8}-{4,7,9}
# print(s1.intersection(s2))

# print(s1.union(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

# d1={
#     "Apple":"Seb",
#     "Name":"Rohan",
#     "Age":67
# }

# print(d1)
# print(type(d1))

# print(d1)
# print(d1["Apple"])
# print(d1["Name"])

# d1={
#     "Apple":"Seb",
#     "Name":"Rohan",
#     "Age":67
# }

# d1["Pranvi"]="Kumari"
# d1["Name"]="Rahul"

# d1.pop("Name")
# d1.popitem()
# d1.clear()
# print(d1)

# for item in d1:
#     print(item)

# for item in d1:
#     print(d1[item])

# for item in d1.keys():
#     print(item)

# for item in d1.values():
#     print(item)

# for key,val in d1.items():
#     print(f"My key is {key} and value is {val}")

# d1={
#     "Apple":"Seb",
#     "Name":"Rohan",
#     "Age":67
# }
# d2={
#     "adhar":1234567890,
#     "roll":101,
# }
# print(d1.get("Name"))
# print(d1["Name"])

# d1.update(d2)
# print(d1)

# age=45

# if (age<0 or age>120):
#     raise ValueError("Age is not Possible")

# if age>18:
#     print("You can drive")
# else:
#     print("You can not drive")

# print("Adult") if age>18 else print("Minor")