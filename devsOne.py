# !/usr/bin/env python3

# operator precedence
# -->>
# (), **, * /, + -
print((20 - 3) * 4 ** 2)

# returns binary
print(bin(5))

# convert bin to num
print(int('0b101',2))

# augmented assignment operator
a = 5
a +=2
print(a)

# long string
strings = '''
dwfaqefqe
qwfqefqef
qfqwergweg
'''
print(strings)

# concatenation (string)
fname = 'Afif'
lname = 'Zuhair'
fullname = fname + ' ' + lname
print(fullname)

# concatenation (mix) + conversion
fname1 = 'Afif'
ic1 = 1234567890
print(fname + str(ic1))

# escape sequence (spec char)
weather = 'It\'s "kind of" sunny'
print(weather)

# formatted strings (f) / .format
name ='Afif'
age = 16

# variables placement
print(f"Hi {name}, you're {age} years old")

# using variables
print("Hi {} , you're {} years old".format(name, age))
# using index order
print("Hi {0} , you're {1} years old".format("Afif", 24))
# using index order (variables)
print("Hi {name} , you're {age} years old".format(name="Afif", age=24))


# STRING INDEXES-----------------------------------------------
selfish = '013456789'
# start from the front
# selfish[start:stop:stepover]
print(selfish[2])
print(selfish[0:5])
print(selfish[0:8:2])
 #start at the end
print(selfish[-2])


# immutability, a value cannot be changed
# cannot reassign to a value assigned initially
# cannot do something like, selfish[8] = '10', instead
selfish = selfish + '10'
print(selfish)

# string length
print(len(selfish))


# BUILT IN FUNCTIONS---------------------------------------

# uppercase
qoute = 'i am groot'
print(qoute.upper())

# find char
print(qoute.find('o'))

# replace
print(qoute.replace('o','a'))

# mix
qoute2 = qoute.replace('o','a')
print(qoute2.upper())

# boolean
name = 'Ahmad'
is_cool = False
print(is_cool)

# type conversion
# birth_year = input("what is your birth year?")
birth_year = 1995
age = 2021 - int(birth_year)
print(f'{name}, your age is {age}')