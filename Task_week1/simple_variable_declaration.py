#Create a program that stores an integer, a floating-point number, a string, and a boolean variable, and then outputs them.
if __name__ == '__main__':
    intValue = 20
    floatValue = 12.5
    stringText = "Hello world"
    booleanValue = True
    print(f"{intValue} + {floatValue} + {stringText} + {booleanValue}")

#Declare and initialize an integer variable `zahl` with the value 10. Check the variable's type afterward
zahl = 10
print(f" data type for zahl is {type(zahl)}")

#Declare and initialize a floating-point variable `kommazahl` with the value 10.5. Check the variable's type afterward.
kommazahl = 10.5
print(f"data type of kommazahl is {type(kommazahl)}")

#Declare and initialize a string variable `text` with the value "Hello, World!". Check the variable's type afterward.
text = "Hello world !"
print(f"the data type of text is {type(text)}")

#Declare and initialize a boolean variable `wahrheitswert` with the value True. Check the variable's type afterward.
wahrheitswert = True
print(f"the data type of wahrheitswert is {type(wahrheitswert)}")  # or isinstance(variable, (int,float)) comparing against the data type
