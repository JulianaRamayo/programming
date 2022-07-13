#Write a Python program to get the volume of a sphere with radius 6.
from math import pi
radious = float(input("please enter the radious of the sphere to obtain the volume: "))
volume = 4.0/3.0*pi* radious**3
print("the volume of the sphere with radious", radious, "is: ", volume)