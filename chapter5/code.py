#this code uses the setdefault function to set a key and value
#to a dictionary if it doesnt exist
period_table = {'Hydrogen': 2, 'helium':3}
print(period_table)

carbon = period_table.setdefault('carbon',12)
print(carbon)
print( period_table)


#using the defaultdict()
#the defaultdict takes an integer and specifies the default 
#value of a new key upfront.
from collections import defaultdict
period_table = defaultdict(int)
period_table['hydrogen'] =1
period_table['lead']
print(period_table)


#The noidea() returns a value to be
# sassigned to the missing key
def no_idea():
    return 'huh'
bestiary = defaultdict(no_idea)
bestiary['a'] = 'hans'
bestiary['b']= 'debrah'
bestiary['c'] = 'john'
bestiary['d']
print(bestiary)


#Using the standard library's counter
from collections import Counter
breakfast = ['spam','spam','eggs','spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

#most_ common counter() returns all elements in
#ascending order
#this code prints the most common elements with counters
mostCommon = breakfast_counter.most_common()
print(mostCommon)


#Ordered by key with orderedDict()
#this code returns the dicrtonary but not in order
quotes = {
       'Moe': 'A wise guy, huh?',
       'Larry': 'Ow!',
       'Curly': 'Nyuk nyuk!',
}
for stooge in quotes:
    print(stooge)
##
##
#using the orderDict remembers the order
from collections import OrderedDict
quotes = OrderedDict([('Moe','A wise man, huh'),
                      ('larry','ow!'),
                      ('curly','Nyuk nyuk'),
                      ])
for stooge in quotes:
    print(stooge)
    
    
#DEQUE
#this code checks to remove the letters from the 
#leftside and right side if they are equal it prints true
#else prints false
def palindrome (word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft()!= dq.pop():
            return False
    return True


#USING ITERTOOLS TO ITERATE OVER CODESTRUCTURES 

import itertools
for item in itertools.chain([1,2],['a','b']):
    print(item)