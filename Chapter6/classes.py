#creating a class Person
class Person():
    def __init__(self,name):
        self.name = name
footballer = Person('Lionel Messi')
print('best player is :',footballer.name)



#defining an empty car class
class Car():  #this is the parent class
    def exclaim(self): #this is a method
        print('Im a car')

class Yugo(Car):  #this class is the sub class
    def exclaim(self):
        print("im a yugo, much like a car ..")
       

#creating an object from each class
give_me_car = Car()
give_me_a_yugo = Yugo()
give_me_car.exclaim()
give_me_a_yugo.exclaim()  #we over rode the inheritance


#Getting help from the parent class with the use of super
#this code use the 

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name,email):
        super().__init__(name)
        self.email = email
Hans = EmailPerson('Hans Donkor','baffourhans@gmai.com')

print(Hans.name)


#private and public methods using get and set
#define a duck class with a single parameter

class Duck ():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print("inside the getter")
        return self.hidden_name
    def set_name(self,input_name):
        print("inside the setter")
    name = property(get_name,set_name)
fowl = Duck("john")
print(fowl.name)

fowl.get_name()
fowl.name = 'kofi'



#defining a circle class that has a radius attr and a 
#computed diameter

class Circle ():
    def __init__(self,radius):
        self.radius = radius
        
        @property
        def diameter(self):
            return 2 * self.radius

c = Circle(4)
print(c.radius)
#print(c.diameter)  #This code does not run , finding the diameter



#Method types. 
# Let’s define a class method for A that
#counts how many object instances have been made from it:


class A():
    count = 0
    def __init__(self):
        A.count +=1
    def exclaim(self):
        print("Im an A")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects")
easy_a = A()
breezy_a =A()
print(A.kids())



#Duck typoing
#polymorphism

class Quote():
    def __init__(self,person,words):
       self.person = person
       self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'
    
class QuestionQuote(Quote):
    def says (self):
        return self.words + "?"
    
class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Hans',"Im hunting dogs")
print (hunter.who(), 'says',hunter.says())

hunted1 = QuestionQuote('bugs bunny', "whats up boy")
print (hunted1.who(), 'says',hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())


#SPECIAL METHODS IN PYTHON
#checks to see if the second and first strings are equal
class Word():
    def __init__(self, text):
        self.text = text
        def __eq__(self, word2):
            return self.text.lower() == word2.text.lower()
first = Word('ha')
second = Word('HA')
third = Word('eh')
first ==second


#Compostion
#making a tail and bill objects and providing them to a new oduck bject

class Bill():
    def __init__(self, description):
        self.description = description
        
class Tail():
    def _init_(self,length):
        self.length = length
        
class Duck():
    def _init_(self,bill, tail):
        self.bill = bill
        self.tail = tail
    def about (self):
        print('This duck has a', bill.description,'bill and a',
              tail.length, 'tail')

