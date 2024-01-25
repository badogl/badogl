import math

print("Hello Welcome to Calc")
c=10000
# Square Calc
def calcSqr(a):
    Sol=a*a
    msqr=Sol/c
    print(f"This square is {Sol} square centimeters, {msqr} square meters\n")

# Rectangle Calc
def calcRec(a,b):
    Sol=a*b
    msqr=Sol/c
    print(f"This rectangle is {Sol} square centimeters, {msqr} square meters\n")
    

# Circle Calc
def calcCircle(r):
    r*=2
    Sol=float(math.pi*r)
    msqr=Sol/c
    
    # We set how many elements will be displayed after the comma
    print(f"This rectangle is {round(Sol,2)} square centimeters, {round(msqr,5)} square meters\n")

# Request from user for square
data1=float(input("What is the length of a side of the square?"))

# Return Solution Sqr
calcSqr(data1)



# Request from user for rectangle
data2=float(input("What is the length of rectangle?"))
data3=float(input("What is the width of the rectangle?"))

# Return Solution for Rec
calcRec(data2,data3)

# Request from user for circle
data4=float(input("What is the radius of the circle?"))

# Return Solution for Circle
calcCircle(data4)

# Just one number
data5=float(input("What is the a length value:"))

# Return Solution Sqr
calcSqr(data5)

# Return Solution for Rec
calcRec(data5,data5)

# Return Solution for Circle
calcCircle(data5)