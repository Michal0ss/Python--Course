# Duck typing = concept where the class of an object is less important than the methods/attributes class is not
# checked if minimum methods/attributes are present "If it walks like a duck, and it quacks like a duck, then it must
# be a duck"

class Duck():
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is qwuacking")


class Chicken():
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is qwuacking")


class Person():
    def cath(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.cath(chicken)
