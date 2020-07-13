class Dog():
    species = "mammal"
    def __init__(self,breed):
        self.breed = breed

#myDog = Dog(breed= "Labrador")
myDog = Dog("Labrador")
#print(myDog.breed)
#print(myDog.species)

class Circle():
    pi=3.14
    def __init__(self,r=1):
        self.r = r
    def area(self):
        return self.r * self.r * Circle.pi
    def setReadius(self,newR):
        self.r = newR

myCircle = Circle(3)
myCircle.setReadius(99)
print(myCircle.area())