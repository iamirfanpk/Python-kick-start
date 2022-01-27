x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
r = x % 2
s = y % 2
if x==y:
    print(x, "and" ,y ,"are equal")
elif x>y:
    print(x, "is greater than", y)    
elif x<y:
    print(x ,"is less than", y) 
if x>0:
    print(x,"is positive")
else:
    print(x,"is negative")
if y>0:
    print(y,"is positive")
else:
    print(y,"is negative")              
if r==1:
    print(x,"is odd")
elif x==0:
    print(x,"is zero")
else:
    print(x,"is even")
if s==1:
    print(y,"is odd")
elif y==0:
    print(y,"is zero")
else:
    print(y,"is even")    