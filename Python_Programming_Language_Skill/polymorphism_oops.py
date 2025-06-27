class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

# Polymorphism in action:
for animal in [Dog(), Cat()]:
    print(animal.make_sound())
