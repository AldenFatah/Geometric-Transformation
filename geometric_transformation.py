#import(s)
import math

#function(s)
def int_input(a):
    return int(input(a))

def transform(x,y,a,b):
    return [x+a,y+b]

def dilate(x,y,c):
    return [x*c,y*c]

def linear(m,c,x):
    return (x*m)+c

def rotate(x,y,deg,a=0,b=0):
    deg = math.radians(deg)
    x,y = transform(x,y,-a,-b)
    return [round((x*math.cos(deg))-(y*math.sin(deg))+a,10),round((x*math.sin(deg))+(y*math.cos(deg))+b,10)]

def mirror(x,y,a,b,c):
    newx = ((((b*b)-(a*a))*x)-(2*a*b*y)+(2*a*c))/((a*a)+(b*b))
    newy = ((((a*a)-(b*b))*y)-(2*a*b*x)+(2*b*c))/((a*a)+(b*b))
    return [newx,newy]

#logics
end = False
while end == True:
    transfomation = input("choose a transformation:\n1.transform\n2.dilate\n3.rotate\n4.mirror\n5.end\nuse the numbers\n:")
    match transfomation:
        case '1':
            print("A point (x,y) trasformed by a vector (a,b)")
            print(transform(int_input('x:'),int_input('y:'),int_input('a:'),int_input('b:')))
        case '2':
            print("A point (x,y) dilated by a number (c)")
            print(dilate(int_input('x:'),int_input('y:'),int_input('c:')))
        case '3':
            print("A point (x,y) rotated by (deg) degrres from the center (a,b)")
            print(rotate(int_input('x:'),int_input('y:'),int_input('deg:'),int_input('a:'),int_input('b:')))
        case '4':
            print("A point (x,y) mirrored trough a line (ax + by = c)")
            print(mirror(int_input('x:'),int_input('y:'),int_input('a:'),int_input('b:'),int_input('c:')))
        case _:
            end = True
