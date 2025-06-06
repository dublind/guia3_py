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

#pagina 55
#muestra el largo de una cadena
word = 'by'
print(len(word))

empty = ''
print(len(empty))

i_am = 'I / m'
print(len(i_am))

multi_line = '''line 1
line 2'''
print(len(multi_line))
                             
                          
 #pagina 56 
 
str1 = 'a'
str2 = 'b'
print(str1 + str2)  # Concatenation
print(5 * str1)  # Repetition
print(str2 * 4)

#pagina 57 nature of strings -ascii

c1 = 'a'
c2 = 'b'
print(ord(c1))  # ASCII value of 'a'
print(ord(c2))  # ASCII value of 'b'
print(chr(97))  # Character for ASCII value 97
print(chr(945)) # Character for ASCII value 945 (Greek letter alpha)

#pagina 58 
#nature of strings -sequences
string = 'silly walks'
for ix in range(len(string)):
    print(string[ix], end=' ')
print()

string = 'silly walks'
for char in string:
    print(char) #pregunta: porque guarda solo hasta dos valores el iterador?
    print(char, end=' ')
print()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0])  # First character
print(alphabet[25])  # Last character
print(alphabet[1:3])  # Slice from index 1 to 2
print(alphabet[1:])  # Slice from index 1 to the end
print(alphabet[:3])  # Slice from the start to index 2
print(alphabet[-1])  # Last character using negative index


#pagina 59
#nature of strings in / not in
#with boolean checks
text = 'abcdefghijklmnopqrstuvwxyz'
print('f' in text)
print('F' in text)  # Case-sensitive check
print('1' in text)
print('ghi' in text)
print('Xyz' in text)

print('a' not in text)
print('A' not in text)
print('1' not in text)
  
#pagina 60
text = 'abcdefghijklmnopqrstuvwxyz'
#del text[0]
#text.append('z')
#text.insert(0, 'a') 
#ninguna de estas operaciones funciona con cadenas de texto

#61 pagina
#nature of strings

text = 'abcdefghijklmnopqrstuvwxyz'
text = "a" + text
text = text + "z"
print(text)  # Concatenation to add characters at the start and end
print(min('aAbByYzZ')) # Minimum character based on ASCII value
print(max('aAbByYzZ'))  # Maximum character based on ASCII value

#pagina 62
#nature of strings -min/max
t = 'the Knights who say Ni!'
print('[', min(t), ']')  # Minimum character
t = [0, 1, 2]
print(min(t))

print('[', max(t), ']')  # Maximum character

#pagina 63
#nature of strings -index()

print('aAbByYzZ'.index('b'))  # Index of first occurrence of 'a'

#pagina 64

print(list('abcabc'))
print('abcabc'.count('b'))

#pagina 66
print('aBcD'.capitalize())

print('Alpha'.capitalize())
print('ALPHA.'.capitalize())
print(' Alpha'.capitalize())

print('['+'alpha'.center(10)+']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' +'gamma'.center(20, '*') + ']')
#pagina 68

if 'epsilon'.endswith('on'):
    print('yes')
else:
    print('no')

t = 'zeta'
print(t.endswith('a'))
print(t.endswith('A'))
print(t.endswith('et'))


#pagina 69
print('Eta'.find('ta'))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))

print('kappa'.find('a',2))

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s
or earlier, when it was popularized by advertisements
for Letraset transfer sheets. It is now used widely
"""
print(txt.find('ipsum'))  # Find 'ipsum' in the text

print('kappa'.find('a',2,4)) # Find 'a' in 'kappa' from index 2 to 4

#pagina 73
print("Imprimiendo cadenas de texto")
print('Mu40'.isalpha()) #esta cadena no es alfanumérica
print('2018'.isdigit()) #esta cadena es numérica
print('nu'.islower()) #esta cadena es minúscula
print('/n'.isspace()) #esta cadena no es un espacio en blanco

#pagina74
print(','.join(['omicron', 'pi', 'rho'])) #une los elementos de la lista con una coma

#pagina 75
print('SiGmA=60'.lower()) #convierte la cadena a minúsculas
print('['+'tau'.lstrip() + ']') #quita los espacios a la izquierda
print('www.cisco.com'.lstrip('w.')) #quita los caracteres 'w' y '.' a la izquierda

#pagina 76
print('this is it'.replace('is', 'are')) #reemplaza 'is' por 'are'
print('this is it'.replace('is', 'are', 1)) #reemplaza solo la primera ocurrencia de 'is'





	

