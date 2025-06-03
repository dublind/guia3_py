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
	

