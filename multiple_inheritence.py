class Animal:
    alive  = True
    def alive(self):
        print('True')
class Rabbit:
    def run(self):
        print('this can run very fast')
class Sleeping:
    def sleep(self):
        print('this animal may sleep')

class Tiger(Animal,Rabbit,Sleeping):
    print('this is tiger class')
#animal = Animal()
#rabbit = Rabbit()
tiger = Tiger() 
print(tiger.alive,tiger.alive(),tiger.run(),tiger.sleep())


