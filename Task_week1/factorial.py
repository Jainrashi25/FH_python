#Create a program which will calculate the factorial
def factorial_function(factValue):
    product = 1
    for i in range (1, factValue):
        product = product * i
    return product
   

if __name__ == '__main__':
    value = input("Input factorial number: ")
    factValue = int(value)      
    result = factorial_function(factValue)
    print (f"factorial of {factValue} is {result}")

  



























'''  
  value = input("Enter the factorial number") # input function takes string as value and returns a string
    factValue = int(value) 
    sum = 1
    for i in range(1, factValue +1): #range (start, stop)
        sum = sum * i
    print (f"factorial of value is {sum}") 
'''
    

   # 5! 5*4*3*2*154
   #
   # 1. value*1     5*1 = sum
   # 2. value*2     sum*2 = sum
   # 3. value*3     sum*3 =sum 
   # 4. value*4
   # 5. value*5




