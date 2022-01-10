class Fruits:
    def vegetables(self):
        print('this is the Fruit class')
        
class Vegetables(Fruits):
    def vegetables(self):
        print('this is vegetable class')
        
v = Vegetables()
#print(v.vegetables())
v.vegetables()
# an object will use its method which is closely associated with itself first before relying on the method that may inherit 
# from the parent class