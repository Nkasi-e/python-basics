# LIST

peopleList = ['Mango', 'Cabinet', 'munchen', 3, 4, 5]

print(peopleList)

# LIST METHOD

number = [67, 9, 1, 3, 4, 5, 6, 8, 57]
number.sort()  # sort list
number.reverse()  # reverse list
number.append(80)  # add to the end of list
# number.clear()  # remove every item from list
print(number)

# DELETING ITEMS FROM LIST

number.remove(80)
number.pop()
# deleting by range would be [0:8] that means from index 0 to index 8
del number[3]

print(number)
