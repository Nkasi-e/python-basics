# A function is a group of statements to perform a specific task

# Import Note located down


def greet():
    print(f'Hello')


greet()

# PARAMETERS AND ARGUMENTS IN FUNCTIONS


def meetUp(venue, time):  # parameters is passed here
    print(f'The event venue is {venue} and the time for the meet up is {time}')


meetUp("Fountain square abuja", '12:45pm')  # Arguments is passed here


# You can also set a default argument but that is going to be in the parameter.. e.g below

def centurion(age=100):
    print(f"this person's age is = {age}")


centurion()

# RETURN VALUES FROM FUNCTIONS


def isAdult(age):
    # if age >= 17:
    #     return True
    # else:
    #     return False
    # the above code can still be written in the pattern below reasons because it's a bolean

    return age > 17


result = isAdult(19)


print(result)


def convertGender(gender='Unknown'):
    if gender.upper() == "F":
        return "Female"
    elif gender.upper() == "M":
        return "Male"
    else:
        return f'{gender} is unknown'


respond = convertGender('Hello')

print(respond)

# Built In functions... add dot(.) notation to see the built in functions
''
[]
{}

# You can import python modules with the import keyword
# Below are ways you can import

# 1: import maths --Maths is just an example it can be any module.
# 2: from maths import isqrt. --Almost similar to javascript destructuring.
