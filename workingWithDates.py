# Working with dates... to work with date, import the datetime module
import datetime
# from datetime import datetime


print(datetime.datetime.now())  # For current date and time
print(datetime.date.today())  # For current date without time
print(datetime.datetime.now().time())  # For current time without date

# FORMATTING DATES WITH PYTHON
now = datetime.datetime.now()
# Formatted date, you can format it anyhow you want
print(now.strftime(' %d %m %Y %H %M %S'))
# The capital B gives you the month name you are in, while the small b abbreviates the month
print(now.strftime(' %d %B %Y %H %M %S'))
print(now.strftime(' %d %b %Y %H %M %S'))
