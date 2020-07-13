# Inheritance
class Animal():
    def __init__(self):
        print("Animal created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")

#mya=Animal()
#mya.whoAmI()
#mya.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("woof!")
    def eat(self):
        print("Dog eating")
#myDog = Dog()
#myDog.whoAmI()
#myDog.eat()
#myDog.bark()

#Special Methods
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: {}, Author: {}, Pages{}".format(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages

b = Book("python","jose",200)
print(len(b))
