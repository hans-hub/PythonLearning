
#comparing with if, elif and else
#Python program that checks the value of the boolean
#variable disaster and prints an appropriate comment:



print("hans")
disaster = True
if disaster:
    print('woe')
else:
    print('whee')

#Tests withing tests
#this program checks the true condition and prints out the statement
furry = True
small = True
if furry:
    if small:
        print('its a cat')
    else:
        print('its a bear')
else:
    if small:
        print('its a skink')
    else:
        print('its a human. Or a hariless bear')


#Using elif if there are more than two possibilites
color = "blue"
if color == "red":
     print("its a tomato")
elif color == "green":
     print("its a green pepper")
elif color == "purple":
     print("the color is nice")
else:
     print("no color dey")



##Checking the true value of a list
#this code checks for empty data structures

some_list = []
if some_list:
    print('not empty')
else:
    print('this is empty')

#LOOPS
#while
#simple loop that prints out numbers from 1 to 5
    count = 1
    while count <=5:
        print (count)
        count +=1

#cancelling a loop with break
#we break out of the loop when the character "q" is typed
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())


#skipping ahead with continue
#reading an integer and printing the square if its odd and skips if its even

while True:
    value = input('Integer, please[q to quit]:')
    if value == 'q': # quits the program
        break
    number = int(value)
    if number %2 ==0:
        continue
    print(number, 'squared is', number*number)


#checking break use with else
#checks a list of  numbers to find even.

numbers = [1,3,5,4]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('found even number', number)
        break
    position +=1
else:
    print('no even number found')



#Printing the letters in a word(cat)
word = 'cat'
for letters in word:
    print(letters)


#iterating throughh the keys of a dictionary and printing out the keys

hans = {'name':'kyei','age':'90','school':'ucc','country':'ghana'}
for value in hans.values():
    print( value)

#using the else in a for loop to verify that the for loop ran to completion

cheeses =  ['hans']
for cheese in cheeses:
    print ('THis shop  has some lovely',cheese)
    break
else:
    print('this is not much of cheese, is it?')


#comprehensions
#list comprehension
number_list = [number for number in range(1,6)]
print(number_list)

# A list of only odd numbers between 1 and 5 using comprehensions
the_list = [number for number in range(1,6) if number %2 == 1]
print(the_list)

#alternative method
odd_list = []
for number in range(1,6):
    if number % 2 ==1:
        odd_list.append(number)
print(odd_list)



#funtions
def do_nothing():
    return True

#this function returns statement to send the value of anuthing back to its caller twice
def echo(anything):
    return anything + ' ' + anything


# this function takes the a color and returns a string that matches with the condition
def message(color):
    if color == 'red':
        return "its a tomato"
    elif color == "green":
        return "green pepper"
    elif color == "purple":
        return "nice color"
    else:
        return "ive never heard of a color" + " " + color + "."


#A function that prints whether a statement is none:
def is_none(thing):
    if thing is None:
        print('its None')
    elif thing:
        print('its true')
    else:
        print('its false')


#positional arguments
#returns the key and value
def menu(wine,entree,dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}


#a function that is expected to run each time with afreshh empty results , add
#argument to it and print a single item list.

def buggy(arg,result=[]):
    result.append(arg)
    print(result)

#gathering positional arguments with *
def print_more(required1,required2,*args):
    print ('need this one:',required1)
    print ('need thisone too:',required2)
    print('all the rest:',args)
    


#funtions with arguments
    #the function takes two numbers , adds them and prints them out
def add_args(arg1, arg2):
    print(arg1 + arg2)

#this funtion takes the add_args function and excutes with the values passed
def run_something_with_args(func,arg1,arg2):
    func(arg1,arg2)


#combining the previous fucntion with the *args and **kwargs

def sum_args(*args):
    return sum (args)
def run_with_positional_args(func,*args):
    return func(*args)


#functions inside other functions
def outer_func(a,b):
    def inner_func(c,d):
        return c + d
    return inner_func(a,b)

#the use of the lambda functions
#the function capitalizes the list of words and appends an exclamation point

def edit_story(words,func):
    for word in words:
        print(func(word))
stairs = ['thud','meow','thud','hiss']
def enliven(word):
    return word.capitalize() + "!"
def upper(word):
    return word.upper() + "@"

#using the lambda in place of the enliven function
# edit_story(stairs, lambda word: word.capitalize() + '!')



#DECORATORS
def document_it(func):
    def new_func(*args,**kwargs):
        print('Runnning function:',func._name_)
        print('positional arguments:',args)
        print('keyword arguments:',kwargs)
        result = func(*args, **args)
        print('result:',result)
        return result
    
              


#catching errors using try and except
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)
