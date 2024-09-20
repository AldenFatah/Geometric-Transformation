#import(s)
import math

#function(s)
def transform(x,y,a,b):
    return [x+a,y+b]

def dilate(x,y,c):
    return [x*c,y*c]

def linear(m,c,x):
    return (x*m)+c

def rotate(x,y,deg,a,b):
    deg = math.radians(deg)
    x,y = transform(x,y,-a,-b)
    return [round((x*math.cos(deg))-(y*math.sin(deg))+a,10),round((x*math.sin(deg))+(y*math.cos(deg))+b,10)]

def mirror(x,y,isinfinite,m=0,c=0):
    if isinfinite == True:
        return [-x,y]
    elif m==0:
        return [y,x]
    else:
        ctwo = 2*c + m*x -y
        newx = (x + m*(y-ctwo))/(m**2 + 1)
        newy = linear(m,ctwo,newx)
        return [newx,newy]

#print(s)
print("")