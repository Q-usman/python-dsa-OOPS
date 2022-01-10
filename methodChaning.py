class Car:
    def turn_on(self):
        print('car is turned on')
        return self
    def drive(self):
        print('u are driving')
        return self
    def brake(self):
        print('u stepped on break')
        return self
# now lets make an object
car = Car()
#car.turn_on().car.drive()       // this will return an error 
#AttributeError: 'NoneType' object has no attribute 'car'


car.turn_on().drive()
# so we have to return self so that it does not give and error