# LOOPS
# Loops allows us to iterate through set, list, dictionary or any data structure


names = ['Nkasi', 'Emmanuel', 'Miranda',
         'Roland', "Jacob", "Lissandra", "Allen"]

grad = {'Neon', 'Chemist', 'Troll', 'Lamda', 'lord gull'}
print(grad)


# FOR LOOP
for name in names:
    print(name)

for nich in grad:
    print(nich)

# Looping through Dictionaries
className = {
    "Emma": {
        "class": "2022",
        "department": "chemical Engineering",
        "school": "Futminna"
    },
    "Miranda": {
        "class": "Graduated",
        "department": "Library",
        "school": "NICN"
    }
}

for key in className:
    print(f"{key} {className[key]}")  # Method 1 of looping a dictionary

# Another Method of looping a dict
for key, value in className.items():
    print(key, value)


# WHILE LOOP
# WHILE loop works a little bit different than the FOR loop

number = 0
while number < 10:
    print(number)
    number += 1
else:
    print(f'While loop ended')


# BREAK AND CONTINUE

# BREAK
number = 0
while number < 10:
    if number == 6:
        print("Good middle count")
        break
    number += 1
    print(f"{number}, Hooray")

# CONTINUE
while number < 20:
    number += 1
    if number < 10:
        continue
    print(number)

# Break and Continue with FOR loop

for n in [1, 2, 3, 4, 5, 6]:
    if n < 5:
        continue
    print(n)


for n in [1, 2, 3, 4, 5, 6]:
    if n == 5:
        break
    print(n)
