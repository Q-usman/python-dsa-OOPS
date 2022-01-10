class Cars:
    # class varaible
    wheels = 4
    def __init__(self, model, place, year):
        self.model = model #instance variable 
        self.place = place #instance variable
        self.year = year   #instance variable

    def drive(self):
        print('driving')
    def stop(self):
        print('stopped')
obj1 = Cars( place = "germany" , year = 2022,model = "ferrari")
print(obj1.wheels)
print(obj1.model,obj1.place,obj1.year)
obj1.drive()
obj1.stop()