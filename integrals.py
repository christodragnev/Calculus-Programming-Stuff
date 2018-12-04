#Christo Dragnev
#11/21/18
#Integrals Using LRAM, RRAM, MRAM

from math import sin, cos,tan,acos,asin,atan
from math import exp,e,pi
from math import log,log10,sqrt,log2

a=float(input("start of range"))
b=float(input("end of range"))
n=int(input("number of rectangles"))
func=input("Input desired function into syntax")

xvals=[]
yvals=[]

w=((b-a)/n)

mX=[]
mY=[]
AS=0

for i in range (0,n+1):
    xvals.append(a+i*w)
    x=xvals[i]
    yvals.append(eval(func))
    
for i in range (0,n):
    mX.append(a+i*w+w/2)
    x=mX[i]
    mY.append(eval(func))

for i in range (0,n-1):
    AS=AS+(yvals[i]+4*mY[i]+yvals[i+1])*(w/6)

LRAM=(sum(yvals)-yvals[-1])*w
RRAM=(sum(yvals)-yvals[0])*w
MRAM=(sum(mY))*w
TrapA=(LRAM+RRAM)/2

print('LRAM is: ',LRAM)
print('RRAM is: ',RRAM)
print('MRAM is: ', MRAM)
print('TrapA is: ', TrapA)
print('AS is: ', AS)

