class Animal:
    def move(self):
        print("Animal is walking")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog is barking")

# Create an instance of Dog
d=Animal()
d = Dog()
d.move()  # This will print "Animal is walking" because Dog inherits from Animal
d.bark()  # This will print "Dog is barking"
