# %%
'''
Homework 1 about Integers and Floats: Write a program that receives an integer, greater than or equal
to 2, from the user and prints whether that number is odd or even.
'''
def solution1():
    num = int(input("Please enter an integer (>= 2): "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

solution1()


# %%
'''
Homework 2 about Integers and Floats: The Fibonacci Sequence is a series of numbers. The first two numbers
are 0 and 1. The next number is found by adding up the two numbers before it.
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13+21 = 34. Write a program
that receives an integer from the user, called n, and prints out Fibonacci series up to n terms.
'''

def solution2():
    num = int(input("Please enter an integer: "))
    a, b = 0, 1

    for _ in range(num):
        print(a, end=" ")
        a, b = b, a + b

solution2()

# %%
'''
Homework 3 about Integers and Floats: Write a program that receives an integer from the user, called n,
and prints the first n prime numbers. For example, if the input is 7, the output should
be: 2, 3, 5, 7, 11, 13, 17.
'''
def solution3():
    n = int(input("Please enter an integer: "))
    num = 2
    output = 0
    while output < n:
        if all(num % i for i in range(2, num)):
            print(num, end=" ")
            output += 1
        num += 1

solution3()


# %%
'''
Homework 4 about Integers and Floats: Write a program that receives two float numbers from the user
and prints their sum, difference, product, and quotient with results rounded to 2 decimal places.
'''
def solution4():
    a = float(input("Please enter first number: "))
    b = float(input("Please enter second number: "))

    print("sum:", round(a + b, 2))
    print("difference:", round(a - b, 2))
    print("product:", round(a * b, 2))
    print("quotient:", round(a / b, 2))

solution4()


# %%
'''
Homework 5 about Integers and Floats: Write a program that receives an integer n from the user and prints
the sum of squares of the first n natural numbers.
For example, if n=3, the output should be 1^2 + 2^2 + 3^2 = 14.
'''
def solution5():
    num = int(input("Please enter an integer: "))
    total = sum(i*i for i in range(1, num+1))
    print("sum of squares:", total)

solution5()


# %%
'''
Homework 6 about Integers and Floats: Write a program that calculates the area and circumference of a circle
given its radius as input (a float).
'''
def solution6():
    radius = float(input("Please enter an integer: "))
    pi = 3.14159
    print("area:", round(pi*radius*radius, 2))
    print("circumference:", round(2*pi*radius, 2))

solution6()


# %%
'''
Homework 7 about Integers and Floats: Write a program that receives a float number from the user
and prints its floor and ceiling values without using math.floor() or math.ceil().
(Hint: Use int casting and condition checks).
'''
def solution7():
    num = float(input("Please enter an integer: "))
    i = int(num)
    floor = i if num >= 0 else i-1
    ceiling = i if num == i else i+1
    print("floor:", floor)
    print("ceiling:", ceiling)

solution7()


# %%
'''
Homework 8 about Integers and Floats: Write a program that converts a temperature given in Celsius
to both Fahrenheit and Kelvin.
'''
def solution8():
    celsius = float(input("Please enter an integer: "))
    print("fahrenheit:", celsius*9/5 + 32)
    print("kelvin:", celsius + 273.15)

solution8()

# %%
'''
Homework 9 about Integers and Floats: Write a program that receives an integer n and computes the sum of its digits.
For example, if n = 753, the output should be 15.
'''
def solution9():
    num = input("Please enter an integer: ")
    total = sum(int(a) for a in num)
    print("Sum of digits:", total)

solution9()


# %%
'''
Homework 10 about Integers and Floats: Write a program that receives two integers a and b,
and prints the greatest common divisor (GCD) using the Euclidean algorithm.
'''
def solution10():
    a = int(input("Please enter an integer a: "))
    b = int(input("Please enter an integer b: "))
    while b:
        a, b = b, a % b
    print("greatest common divisor:", a)

solution10()
