
#exercise- create a class 
class Vehicle():
    def __init__(self, vin, make, model, color='white'): #parameters to a function, these are placeholders
        self.vin = vin #defining all of the keys on the object
        self.make = make
        self.model = model 
        self.running = False #property is the same value for evry object, so False, the intial value is set here
        self.color = color

    def start(self):
        self.running = True
        print('running')
   
    def stop(self):
        self.running = False
        print('not running')

car = Vehicle('TS123', 'Tesla', 'Model S')
print(car)
print(car.running) # -> False
car.start()
print(car.running) # -> True
plane = Vehicle('X99Y', 'Boeing', '747-B')
print(plane.vin, plane.make, plane.model)



#classes are used to create objects 
#encapsulation: attributes and methods together

# print(dir([]))

#defining a class
#init function, creates internal dictionary of objects, when the class gets instantiated, making an object from the class

#can add attributes to the class itself
class Dog():

    # class attribute
    next_id = 1

    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
        self.id = Dog.next_id #set the instance id 
        Dog.next_id += 1
    def bark(self):
        print(f"{self.name} says woof!") #gets called when we print an instance of the class

    #can overwrite methods
    # def __str__(self):
    #     return f"Dog name {self.name} is {self.age} years old"
    
    # updated __str__
    def __str__(self):
        return f'Dog ({self.id}) named {self.name} is {self.age} years old'
    @classmethod 
    def get_total_dogs(cls):
        return cls.next_id -1 
ragnar = Dog('ragnar')
print(ragnar)
print(ragnar.next_id)
#function gets called when we instantiate a class
#ragnar is a variable that contains an object from the Dog class
ragnar = Dog('ragnar')
# hailey = Dog('hailey', 1)
# print(dir(ragnar)) #dir method is envoking the property that exists on every single object so we can see them
# print(ragnar)
# print(ragnar.next_id)
# print(vars(ragnar))
#can call dir on any datatype, everything is an object

#properties and attributes are interchangeable 

#class methods


#inheritance
#only for classes, camel case
# Pass in superclass as argument
class ShowDog(Dog):
  # Add additional parameters AFTER those in the superclass
  def __init__(self, name, age = 0, total_earnings = 0):
    # Always call the superclass's __init__ first
    Dog.__init__(self, name, age) #getting the object from the Dog class
    # Now add any new attributes
    self.total_earnings = total_earnings
  
  # Add additional methods
  def add_prize_money(self, amount):
    self.total_earnings += amount
betsy = ShowDog('betsy', 4, 4000)
print(dir(betsy))
print(dir(ragnar))