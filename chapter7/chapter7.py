#A test function that takes a python Unicode
#character,, looks up its name, and looks up the character again from the name (it should
#match the original character)

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value="%s"' % (value,name, value2))



#Adding a string by code or by name
my_Name = 'Han\N{LATIN SMALL LETTER S WITH ACUTE}'


#encoding anything in UTF-8
snowman = '\u2603'
#use the following code to check the length and the encoding
print(len(snowman))
ds = snowman.encode('utf-8')
print(ds)


#decoding byte strings to Unicode

#create a unicode string called place

place = 'caf\u00e9'
print(place)


#string formatting
#conversion types

'%s' % 42  # this should be run in the shell, converts 42 to a string


#string and integer interpolation

actor = 'Hans'
cat = 'debrah'
weight = '78'
print("my wifes best friend is %s" %actor)
print("Our cat %s weighs %s pounds" % (cat, weight))


#New style formatting with {}
# this code does the formatting in the new way using the{}
n = 42
f = 7.03
s = 'string cheese'

info = '{} {} {}'.format(n,f,s)
print(info)

#In this example {0} is the entire dictioanry where {1}
# is the string 'other' that follow

d = {'n':42, 'f':7.03, 's':'string cheese'}
new = '{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other')
print(new)



#Regular Expression
#exact  match with match()
#match works only at the begining
import re
source = 'Young Frankenstein'
m = re.match('You', source) #match starts at the beginning of the sourde
if m:              #match returns an object
    print(m.group())
    
    
    #match starts at the begining that is wwhy this does not return anything
source = 'Young Frankenstein'
m = re.match('Frank', source) #match starts at the beginning of the sourde
if m:              #match returns an object
    print(m.group())
    
    
#search gets the pattern from anywhere
source = 'Young Frankenstein'
m = re.search('Frank', source) #match starts at the beginning of the sourde
if m:              #match returns an object
    print(m.group())
    
    
    
#changing the pattern

source = 'Young Frankenstein'
m = re.match('.*Frank', source) #match starts at the beginning of the sourde
if m:              #match returns an object
    print(m.group())
    
    
#using findall for the matching
#using findall to find the number of instances of a single letter
m = re.findall('n',source)
print('Found', len(m),'matches')


#"n' followed by any character
m = re.findall('n.', source)
print(m)

#USING SPLIT TO SPLIT THE RETUTN LIST
#The example that follows shows you how to split a string into a list by a pattern rather
#than a simple string (as the normal string split() method would do):

m = re.split('n', source)
print(m)


#using the sub() to replace paterns

m = re.sub('n', '?', source)




#Special Characters
import string
printable = string.printable
length = len(printable)
print(length)
p = printable[0:50]
print(p)


# to find the digits in the printable

digits = re.findall('\d', printable)
print(digits)

#to find characters which are digits, letters and underscore
a = re.findall('\w', printable)
print(a)


#Patterns using specifiers

source1 = ''' I wish I may , I wish I might .....have a dish of fish tonight..'''

#finding wish anywhere

v = re.findall('wish', source1)
print(v)

#finding wish then fish anywhere
c = re.findall('wish|fish',source1)
print(c)

#finding wish at the begining
i = re.findall('^wish',source1)
print(i)


#finding fish at the end
z = re.findall('fish$',source1)
print(z)


#begin by finding w or followed by ish
o = re.findall('[wf]ish',source1)
print(o)

#Bytes and Byte arrays
#creating bytes and bytearrays out of a list

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)



#denonstration that a byte cant be changed
# this cide gives out a typerror
the_bytes[1] =  127
