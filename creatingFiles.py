# WORKING WITH FILES

# CREATING A FILE
# "w" means writing to a file and this will AUTOMATICALLY create a file if  the file doesn't exist.
file = open('./data.csv', "w")


# OPEN A FILE FOR READING AND WRITING
# "r+" signifies that you want to read and write the file while "r" signifies that you just want to read alone
file = open('./data.csv', "r+")
file.write("id, name, email\n")  # writing on/to the file
file.write("1, Miranda, email@gmail.com\n")  # writing on/to the file
file.write("2, Emma, email@gmail.com\n")  # writing on/to the file

# APPEND TO A FILE
file = open('./data.csv', "a")
file.write("3, Roland, email@gmail.com\n")


# READING FROM FILES
file = open('./data.csv', "r")
print(file.read())

# Reading Line by Line
# for line in file:
#     print(line)
print(file.readlines())


# Note: Anytime you work with files and you perform any operation on them you need to close the file
file.close()  # For closing the file


# BETTER WAY TO WORK WITH FILES
