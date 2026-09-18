from math import pi
if __name__ == '__main__':

    inValue = input( "Input the radius of the circle :") # input is just a function to take input from console
    radius = float(inValue)
    area = pi * radius ** 2 # ** to the power of 
    print (f"Area of circle is {area}") 

    #print(f"The area of the circle with radius {radius} is {pi * radius ** 2}") 