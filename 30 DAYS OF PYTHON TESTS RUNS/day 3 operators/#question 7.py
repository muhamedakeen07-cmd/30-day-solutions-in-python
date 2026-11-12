#question 7
#  Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math 
r = float(input("Enter the Radius: "))



area = math.pi * r * r 
circumference = 2 * math.pi * r

print(area)
print(circumference)