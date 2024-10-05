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
while end != True:
    transfomation = input(
        """choose a transformation
        1.transform
        2.dilate
        3.rotate
        4.mirror
        5.end
        use the numbers
        :""")
    match transfomation:
        case '1':
            print(transform(int_input('x:'),int_input('y:'),int_input('a:'),int_input('b:')))
        case '2':
            print(dilate(int_input('x:'),int_input('y:'),int_input('c:')))
        case '3':
            print(rotate(int_input('x:'),int_input('y:'),int_input('deg:'),int_input('a:'),int_input('b:')))
        case '4':
            print(mirror())
        case _:
            end = True
