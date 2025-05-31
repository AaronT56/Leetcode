class MyObject:
    def greet(self):
        print("Hello!")

    def add(self, x, y):
        return x + y

# Create an instance (object) of MyObject
obj = MyObject()

# Call methods on the object
obj.greet()            # prints "Hello!"
result = obj.add(3, 4) # result = 7
print(result)