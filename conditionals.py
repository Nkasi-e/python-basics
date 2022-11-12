# IF STATEMENTS
name = 8
number = 0
if name > 12 or name == 8:
    print(f"Hello {name}")
else:
    print(f"{name} not valid")

if (number > 0):
    print(f'{number} is positive')
elif number == 0:
    print(f'{number} is null')
else:
    print(f'{number} is negative')


# TERNARY IF STATEMENTS

message = "Positive number" if number > 0 else "Negative number"
print(message)
