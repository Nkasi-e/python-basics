import keyword

# print("hello Nkasi")
# creating variables in python
# name = "Nkasi"  # str
# age = 20  # int
# numbers = []  # list
# pi = 3.14  # float
# isAdult = True  # bool

# DATA TYPES
# print(type(name))  # string str
# print(type(age))
# print(type(numbers))
# print(type(pi))
# print(type(isAdult))

# METHODS IN STRING
brand = 'Nkasi foundation'
print(brand.upper())  # to uppercase
print(len(brand))  # gives back the length of the variable
print('code' in brand)  # to check if code is in brand
print('code'not in brand)  # to check if code is not in brand

# MULTILINE AND FORMATTING STRINGS
# comment = 'Making this comment \n good literally'
# talk = """
# comments can be tedious
# and I dont fancy them
# meaning there is lot to do
# """

# print(comment)
# print(talk)

# name = 'Nkasi'


# message = f"hello {name}, hope you are doing good and {6+9} years old"
# print(message)

# INDENTATION
# In python code must be indented to work properly unlike javascript

# def my_function():
#     name = 'my name'
#     age = 45

# RESERVED KEYWORDS
# this give a list of reserved keywords that can't be used when writing code but can be used when constructing your code
print(keyword.kwlist)


# ARITHMETIC OPERATORS

# print(1 + 4)
# print(1 / 4)
# print(1 * 4)
# print(1 % 4)
# print(1 - 4)

# COMPARISON OPERATORS
print(10 > 4)
print(10 >= 4)
print(10 < 4)
print(10 <= 4)
print(10 == 4)
print(10 != 4)

# LOGICAL OPERATORS
# Basically you can combine all of the expression and use them all together
print((10 < 4) or (3 < 6) and "A" == "A")

# one of the conditions must be met for it to evaluate to true
print((10 < 4) or (3 < 6) or "A" == "A")


# All the conditions must be met for it to evaluate to true
print((10 > 4) and (3 < 6) and "A" == "H")

print(not ("Nkasi" == "Emmanuel"))
# The not operator reverses the expression to the opposite


# ASSIGNMENT OPERATOR
# cosmos = "Apple"
# cosmos = 'samsung'
# numbers = 5
# numbers += 1
# numbers -= 1
# numbers *= 1
# numbers /= 2
# numbers **= 2

# print(numbers)
# print(cosmos)
