# Set is so much similar to a list but in set duplicates are not allowed unlike a list where items in it can be duplicated. see the difference below
# Note: In set you have curly bracket instead of square brackets and in set the order is not guaranteed


# List
numbersList = [1, 2, 3, 4, 5, 5]

# Set
numbersSet = {1, 1, 3, 4, 4, 5, 5}

print(numbersList)
print(numbersSet)

# If you don't want duplicates use a SET{} otherwise use a LIST[]

# SET UNION | INTERSECTION & DIFFERENCE

# UNION
# This simply means the combination of two set, it takes everything from both or multiple SETS and puts it in another set

letterA = {"a", "b", "c"}
letterB = {"b", "f", "g"}

union = letterA | letterB


# INTERSECTION
# to use intersection you simply have the & sign, intersection returns the common value within the both set or what occurs in both set.

intersection = letterA & letterB


# DIFFERENCE
# Difference show or return the differnt value between both set

difference = letterA - letterB

print(difference)


print(f'Union = {union},')
print(f'Intersection = {intersection},')
