class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def __init__(self):
        print("Dog Created")

    def bark(self):
        print("WHOOF!")

    def who_am_i(self):
        print("I am a Dog")


dog = Dog()

dog.who_am_i()
dog.eat()
dog.bark()
