# %%
'''
Homework 1 about Conditionals: Write a program that receives an integer from the user and prints
Large if that number is greater than or equal to 100, prints average if that number is between 20 and 100,
and prints Small if that number is less than or equal to 20. You can get an input from user and convert
it to an integer using a = int(input('Please enter an integer:')).
'''
a = int(input('Please enter an integer:'))
def solution1(a):
    if a >=  100:
        print("Large")
    elif a > 20:
        print("average")
    else:
        print("Small")

# to run 
solution1(a)
    


# %%
'''
Homework 2 about Conditionals: Write a program that receives an integer from the user and prints Positive 
Even, Positive Odd, Negative Even, or Negative Odd, depending on the number. You can get an input from user 
and convert it to an integer using a = int(input('Please enter an integer:')).
'''
a = int(input('Please enter an integer:'))
def soltuion2(a):
    if a % 2 == 0 and a > 0:
        print('Positive Even')
    elif a % 2 != 0 and a > 0:
        print('Positive Odd')
    elif a % 2 == 0 and a < 0:
        print('Negative Even')
    elif a % 2 != 0 and a < 0:
        print('Negative Odd')
    else:
        print('its Zero can be both negative and positve even')

# to run this 
soltuion2(a)
    

# %%
'''
Homework 3 about Conditionals: Write a program that asks the user for their exam score (0–100) 
and prints the letter grade: A (90–100), B (80–89), C (70–79), D (60–69), or F (below 60).
'''
exam_score = int(input("What's your exam score:"))
def solution3(score):
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
solution3(exam_score)


# %%
'''
Homework 4 about Conditionals: Write a program that asks for the year and prints "Leap Year" 
if it is divisible by 4 but not by 100, OR divisible by 400. Otherwise, print "Not a Leap Year".
'''

year = int(input("Enter a year: "))

def solution4(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print('Not a Leap Year')
solution4(year)


# %%
'''
Homework 5 about Conditionals: Write a program that asks the user for a temperature in Celsius. 
If temperature is less than 0, print "Freezing". If between 0 and 30, print "Normal". 
If greater than or equal to 30, print "Hot".
'''

temperature = int(input("May I know the temperature  in Celsius:"))

def solution5(temp):
    if temp < 0:
        print('Freezing')
    elif temp < 30:
        print('Normal')
    else:
        print('Hot')

solution5(temperature)

# %%
'''
Homework 6 about Conditionals: Write a program that asks the user to enter three integers. 
Print the largest number among them using conditionals.
'''
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

def solution6(a, b, c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    
    print(largest)

solution6(num1, num2, num3)


# %%
'''
Homework 7 about Conditionals: Write a program that asks the user to enter a character. 
Check whether it is a vowel (a, e, i, o, u) or a consonant.
'''
character = input("Enter a single character: ").lower()

def solution7(char):
    if char in 'aeiou':
        print("vowel")
    else:
        print("consonant")
solution7(character)



# %%

'''
Homework 8 about Conditionals: Write a program that receives an integer from the user and checks 
if it is divisible by both 3 and 5, only by 3, only by 5, or by neither.
'''
integer = int(input("Enter an integer: "))

def solution8(num):
    if num % 3 == 0 and num % 5 == 0:
        print("both 3 and 5")
    elif num % 3 == 0:
        print("only 3")
    elif num % 5 == 0:
        print("only 5")
    else:
        print("Neither")
solution8(integer)


# %%
'''
Homework 9 about Conditionals: Write a program that asks for the user’s age. 
If age < 13, print "Child". If 13–19, print "Teenager". If 20–64, print "Adult". If 65 or more, print "Senior".
'''
age = int(input("Enter your age: "))

def solution9(num):
    if age < 13:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")
solution9(age)



# %%
'''
Homework 10 about Conditionals: Write a program that asks the user for two integers 
and prints whether the first is greater, smaller, or equal to the second.
'''

num1 = int(input("Enter the first_int: "))
num2 = int(input("Enter the sec_int: "))

def solution10(a, b):
    if a > b:
        print("First number is greater")
    elif a < b:
        print("First number is smaller")
    else:
        print("First equal to  second")
solution10(num1, num2)

