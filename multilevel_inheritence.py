class Animal:
    alive = True
class Fish(Animal):
    def swim(self):
        print('this can swm')
class Tuna(Fish):
    print('this can also swm')

t = Tuna()
print(t.alive, t.swim())

# in multilevel we can hererchy of the inheritence from grand parent to parent ot child  and so on