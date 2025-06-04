#pagina 8
from math import sin ,pi
print(sin(pi))

print(sin(pi / 2))

# pagina 10
import math
for name in dir(math):
	print(name, end='\t')

# pagina 11
from math import pi, radians, degrees, sin, cos, tan, asin
ad = 90
ar =radians(ad)
ad =degrees
print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

# pagina 12
from random import random 

for i in range(5):
	print(random())
from random import random, seed
seed(0)
for i in range(5):
	print(random())

from random import  choice, sample

lst = [1, 2, 3, 4, 5]
print(choice(lst))
print(sample(lst, 3))
print(sample(lst, 3, counts=[1, 1, 1, 1, 1]))

#pagina 14
print(" \n ---PAGINA 14---")
from platform import platform 
print(platform())

from platform import version 
print(version())

from platform import machine
print(machine())

from platform import processor
print(processor())

from platform import system
print(system())

print(__name__)

if __name__ == "__main__":
	print("This is the main module.")
else:
	print("This module is being imported.")

#pagina 19
counter = 0

if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I loke to be a module")

from module import __counter

print(__counter)

#pagina 28

import math 
x = float(input("Enter x: "))
y = math.sqrt(x)
print("square root of", x, "equals to: ", y)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
if b != 0:
    print(a/b)
else:
    print("It cannot be done")
print("THE END")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
try:
    print(a/b)
except:
    print("It cannot be done")
print("THE END")

#pagina 33
try:
    print("1")
    x = 1 / 0
    print("2")
except: #como no puede dividir por cero, se ejecuta el except
    print("oh dear")
print("3")

#pagina 34
try:
    x = int(input())
    y = 1 / x
except:
    print("oh dear, something went wrong!")
print("THE END")

#pagina 35
try:
    x = int(input())
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("oh dear, you cannot divide by zero!")
except ValueError:
    print("oh dear, you must enter a  integer number!")
except:
    print("oh dear, something went wrong!")
print("tHE END")

#pagina 36
try:
    x = int(input())
    y = 1 / x
    print(y)
except ValueError:
    print("oh dear, you must enter a  integer number!")
except:
    print("oh dear, something went wrong!")
print("THE END")

try:
    x = int(input())
    y = 1 / x
    print(y)
except ValueError:
    print("oh dear, you must enter a  integer number!")
print("THE END")

# pagina 38
try:
    y = 1 / 0
except ZeroDivisionError:
    print("oh dear, you cannot divide by zero!")
print("THE END")

# pagina 39
try:
    y = 1 / 0
except ArithmeticError:
    print("arithmetic error")
except ZeroDivisionError:
    print("oh dear, you cannot divide by zero!")
print("THE END")

#pagina 40
def badfun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("sorry for arithmetic error")
    return None

badfun(0)
print("THE END")
#pagina 41
def badfun(n):
    return 1 / n

try:
    badfun(0)
except ArithmeticError:
    print("what did you do")
print("THE END")

#pagina 42
def badfun(n):
    raise ZeroDivisionError

try:
    badfun(0)
except ArithmeticError:
    print("what did you do?")

print("THE END")

"#pagina 43"

def badfun(n):
    try:
        return n/0
    except ArithmeticError:
        print("i see!")
    print("THE END")

#pagina 44
import math
x = float(input("Enter x: "))
assert x >= 0.0
x = math.sqrt(x)
print(x)

from math import tan, radians
angle = int(input("Enter the angle in degrees: "))
#we must be sure that angle != 90 + k*180
assert angle % 180 != 90
print(tan(radians(angle)))

#the code shows an extravagant way of leaving the loop
list = [1, 2, 3, 4, 5]
ix = 0
doit = True
while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False
print("done")

#pagina 47
#this code cannot be terminated by pressing Ctrl-C
from time import sleep
seconds = 1
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("don't do that")


#pagina 48
#this code caouses the memoryerror exception
#warning: executing this codemay be crucial for yours os
#don't run it in production environments!

string = "x"
try:
    while True:
        string += string
        print(len(string))
except MemoryError:
    print("this is not funny!")

#the code print subsequent values of exp(k), k=1,2,4,8,16
from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print("number is too big")

#one of this imports will fail - which one?
try:
    import math
    import time
    import abracadabra
except:
    print("one of your imports has failed")

#how to abuse the dictionary and how to deal with it
dict = {'a' : 'b', 'b' : 'c', 'c' : 'd'}
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print("no such key: ", ch)




	

