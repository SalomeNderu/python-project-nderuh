num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
#for loop that traverses numbers from 1 to 100
for x in range(num1,num2):
  #check if number is divisible by both 3 and 5
  if(x%3==0 and x%5==0):
    print(x,"FizzBuzz")
  #check if number is divisible by 3
  elif(x%3 == 0):
    print(x,"Fizz")
  #check if number is divisible by 5
  elif(x%5 == 0):
    print(x,"Buzz")
  #if not divisible by either of them print the x
  else:
    print(x)