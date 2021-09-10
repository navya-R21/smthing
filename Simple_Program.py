
#1.
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

print(Person.age)
p=Person()
p.greet()

#2
class Snake:
    name = "python"
    def change_name(self, new_name):
         self.name = new_name
s= Snake()
# print the current object name
print(s.name)
# change the name using the change_name method
s.change_name("anaconda")
print(s.name)

#3
class Fruit:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

a =Fruit("apple")
b=Fruit("mango")
print(a.name)
print(b.name)

#polymorphism
def add(x, y, z=0):
    return x + y + z
print(add(2, 3))
print(add(2, 3, 4))

#polymorphism usig methods
class ant():
	def capital(self):
		print("ant house")

	def language(self):
		print("ant language .")

	def type(self):
		print("Insects.")

class Elephant():
	def capital(self):
		print("forest.")

	def language(self):
		print("shout.")

	def type(self):
		print("strong animal.")

obj_ant = ant()
obj_Elephant = Elephant()
for country in (obj_ant, obj_Elephant):
	country.capital()
	country.language()
	country.type()

#encapsulation
class Number(object):
   def __init__(self):
      self.__version = 22

   def getVersion(self):
      print(self.__version)

   def setVersion(self, version):
      self.__version = version

obj = Number()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()

#Abstraction-  We need to import the abc module, which provides the base for defining Abstract Base classes (ABC).
# The ABC works by decorating methods of the base class as abstract.
from abc import ABC, abstractmethod
class Car(ABC):
	def mileage(self):
		pass
class Tesla(Car):
	def mileage(self):
		print("The mileage is 30kmph")
class Suzuki(Car):
	def mileage(self):
		print("The mileage is 25kmph ")
class Duster(Car):
	def mileage(self):
		print("The mileage is 24kmph ")
class Renault(Car):
	def mileage(self):
		print("The mileage is 27kmph ")

t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

#global namespace
var1 = 5
def some_func():
	# local namespace
	var2 = 6
	def some_inner_func():
		#nested local namespace
		var3 = 7
print(var1)

# global variable
count = 5
def some_method():
	global count
	count = count + 1
	print(count)
some_method()

