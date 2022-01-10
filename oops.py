class Car:
    # make = None
    def __init__(self, model,make):
        self.model =  model
        self.make = make
    # pass
    def drive(self, new1):
        #self.new1 = new1
        #print(self.model,'car is runiing')
        print(new1)
    def stop(self,new1):
        #self.new1 = new1
        #print(self.model,'car is stopped')
        print(new1)
myObj = Car('ferrari', 'dubai')
#print(myObj.model)
# print(myObj.make)
print(myObj.drive(5))
obj2 = Car('bmw' , 'chennai')
# print(obj2.model)
# print(obj2.make)
print(obj2.stop(2))