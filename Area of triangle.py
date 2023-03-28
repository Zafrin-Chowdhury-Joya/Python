import math
#1st Way
height= float(input("Enter the height of the Triangle : "))

base = float(input("Enter the base of the Triangle : "))

area = (height*base)/2
print("Area of the Triangle : ", area)

#2nd Way
a = float(input("Enter the first side of the triangle :" ))
b = float(input("Enter the 2nd side of the triangle :"))
c = float (input ("Enter the 3rd side of the triangle :" ))
perimeter= a+b+c
s= perimeter/2
area1 = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Perimeter of the Triangle : ", perimeter)

print ("Area of the Triangle :", area1)