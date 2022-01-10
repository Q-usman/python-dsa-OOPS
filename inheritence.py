'''
    classes can have children
    children clases will inherit every thing what their parent have
    all of the parents attribute and methods
    not only that children classes can implement their own attribute     and methods
'''
class Animal:
    alive = True
    def __init__(self,age):
        print(self)
        self.alive = False
        self.age = age
        print(self.alive, self.age)
    def eat(self):
        print('this animal is eating')
    def sleep(self):
        print('this animal is sleeping')
class Rabbit(Animal):
    #print(alive)
    alive = False
    def runing(self):
        print('this rabbit is runnng')
animal = Animal(1)
rabbit = Rabbit(2)
Rabbit(3)
#print(rabbit.alive)
