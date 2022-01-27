from math import pi
def Area_of_circle(r):
    A = pi*(r**2)
    return A
def Area_of_rectangle(l,b):
    A = l*b
    return A
def Area_of_sqaure(l):
    A = l**2
    return A 
def Area_of_triangle(b,h):
    A = (1/2)*b*h
    return A       
print("Menu")
print()
print("1. Area of Circle \n2. Area of Rectangle \n3. Area of Square \n4. Area of Triangle")
print()
Option = int(input("Enter your option : "))
if Option == 1:
    radius = int(input("Enter Radius of your cirlce(c.m) : "))
    Area_of_your_circle = Area_of_circle(radius)
    print(f"Area of your circle : {Area_of_your_circle}")
elif Option == 2:
    length = int(input("Enter lenght of the rectangle : "))
    breadth = int(input("Enter breath of the rectangle : "))
    Area_of_your_rectangle = Area_of_rectangle(length,breadth)
    print(f"Area of your rectangle : {Area_of_your_rectangle}")
elif Option == 3:
    length = int(input("Enter lenght of the sqaure : "))
    Area_of_your_sqaure = Area_of_sqaure(length)
    print(f"Area of your sqaure : {Area_of_your_sqaure}")
elif Option == 4:
    breadth = int(input("Enter breath of the triangle : "))
    hight = int(input("Enter hight of the triangle : "))
    Area_of_your_triangle = Area_of_triangle(breadth,hight)
    print(f"Area of your triangle : {Area_of_your_triangle}")