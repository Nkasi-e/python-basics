# CLASSES
# Classes are blueprints for creating anything you can think of, maybe a document or date collections in the real world. In simple classes are blueprints that allows you to create objects
# With classes we specify the attributes, attributes are anything that resembles your data or connected to your data objects. Behaviours are what the actual object can do. With classes you can model any object you want. And this is the world of OBJECT ORIENTED PROGRAMMING (OOP)

# OOP involves you creating a bunch of classes and then connecting them together

# OBJECT
# Objects are real life modelled data

# CREATING CLASSES (OOP)

class Phone:
    def __init__(self, brand, price) -> None:
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

    # Override method so as to print the object properly by converting it to string
    # PRINTING OBJECTS PROPERLY
    def __str__(self) -> str:
        return f'Brand {self.brand} Price = {self.price}'

# Creating an instance to use the class object created above


iPhone = Phone("iPhone 14", 1500)
samsung = Phone("Samsung Z Flip", 3000)

print(iPhone)
print(samsung)
iPhone.call('7978797')
samsung.call('eciucicciucdc')

# def __init__(self) is a constructor and the self binds object to the program, self is similar to this in javascript
