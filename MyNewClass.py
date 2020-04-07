class MyNewClass:
    """This class demonstrates the creation of objects"""

    # instance attribute
    num = 100

    # instance method
    def hello(self):
        print("Hello World!")


# creating object of MyNewClass
obj = MyNewClass()

# prints attribute value
print(obj.num)

# calling method hello()
obj.hello()

# prints docstring
print(MyNewClass.__doc__)
