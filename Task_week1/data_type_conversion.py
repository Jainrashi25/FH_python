if __name__ == '__main__':
   intValue = 0
   floatValue = 12.5
   stringText = "45"
   booleanValue = True 

   # Convert an integer to a floating-point number.
   int_to_float = float(intValue)
   print(f"int to float is {int_to_float}")

   # Convert a floating-point number to an integer.
   float_to_int = int(floatValue)
   print(f" float to int is {float_to_int}")

   #Convert an integer to a string.
   int_to_string = str(intValue)
   print(f" int to string is {int_to_string}")

   #Convert a string containing a number to an integer.
   string_to_int = int(stringText)
   print(f" string to int is {string_to_int}")

   #Convert an integer to a Boolean
   int_to_boolean = bool(intValue)
   print(f" int to boolean value is {int_to_boolean}")
