#Christo Dragnev
#11/21/18
#Integrals Using LRAM, RRAM, MRAM

from math import sin, cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2

func = input("Enter function: ")
a = float(input("Enter a lower bound: "))
b = float(input("Enter a upper bound: "))
n = int(input("Enter a whole number of boxes: "))
Width = (b-a)/n

LRAM = 0
xValue =  a
while xValue < b:
    x = xValue
    y = eval(func)
    LRAM += y*Width
    xValue += Width
print("LRAM: ",LRAM)

RRAM = 0
xValue =  a
while xValue < b:
    x = xValue+Width
    y = eval(func)
    RRAM += y*Width
    xValue += Width
print("RRAM: ",RRAM)

MRAM = 0
xValue =  a
while xValue < b:
    x = xValue+Width/2
    y = eval(func)
    MRAM += y*Width
    xValue += Width
print("MRAM: ",MRAM)


