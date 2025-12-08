# %%
'''
Homework 1 about Loops: Write a for loop that iterates through numbers from 1 to 10 using the range
function, adds them up together, and prints the total. The printed output should be 55.
'''
result = 0
for i in range(1, 11):
    result += i
print(result)


# %%
'''
Homework 2 about Loops: Write a program that receives an integer input from the user and call it n. Use a
for loop and an if condition, to find the summation of all numbers that are not a
multiple of 3, from 1 to n, including 1 and n and print the result. For instance, the output of your
program for 9 should be 27 and for 17 should be 108.
'''
n = int(input("Enter an integer: "))

result = 0
for i in range(1, n + 1):
    if i % 3 != 0:
        result += i
print(result)


# %%
'''
Homework 3 about Loops: Write a program that takes an integer input n from the user and prints
the factorial of n using a while loop. Do not use Python’s built-in factorial function.
'''
n = int(input("Enter an integer: "))
factorial = 1
counter = 1
while counter <= n:
    factorial *= counter
    counter += 1
print(factorial)

# %%
'''
Homework 4 about Loops: Using a for loop and the continue statement, print all numbers
from 1 to 50, but skip numbers divisible by both 2 and 5.
'''

def solution4():
    for i in range(1, 51):
        if i % 2 == 0 and i % 5 == 0:
            continue
        print(i)
solution4()

# %%
'''
Homework 5 about Loops: Write a program that repeatedly asks the user to enter a number.
If the number is negative, use the break statement to stop the loop and print "Loop terminated".
Otherwise, print the square of the number.
'''

while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter again:")
        continue
    if number < 0:
        print("Loop terminated")
        break
    else:
        print(number * number)



# %%
'''
Homework 6 about Loops: Write a program that uses a for loop to iterate through numbers 1–100
and calculates the sum of all even numbers. However, if the running sum exceeds 1000, use the break
statement to stop the loop and print the sum at that point.
'''
result = 0
limit = 1000

for i in range(1, 101):
    if i % 2 == 0:
        total_sum += i
        if total_sum > limit:
            break

print(total_sum)


# %%
'''
Homework 7 about Loops: Write a program that prints the first n numbers in the Fibonacci sequence
using a while loop. The program should stop once the count reaches n, where n is entered by the user.
'''

n = int(input('Enter num:'))
a, b = 0, 1
count = 0

while count < n:
    print(a)
    a, b = b, a + b
    count += 1


# %%
'''
Homework 8 about Loops: Write a program that iterates through a given string (entered by the user).
Count how many vowels appear in the string, but use continue to skip over spaces or punctuation marks.
'''

text = input('Enter a string:').lower()
vowels = 0
for char in text:
    if char == ' ' or char in ".,!?":
        continue
    if char in 'aeiou':
        vowels += 1
print(vowels)



# %%
'''
Homework 9 about Loops: Write a program using a nested for loop that prints a multiplication
table from 1 to 10. Format the output so that the table appears neatly aligned.
'''

def solution9():
    for i in range(1, 11):
        row_output = f"{i:2} |"
        for j in range(1, 11):
            product = i * j
            row_output += f"{product:4}" 
        print(row_output)

solution9()
# %%
'''
Homework 10 about Loops: Write a program that simulates rolling a die repeatedly until a 6 appears.
Use a while loop and the break statement to stop rolling. Print how many rolls it took before the first 6 appeared.
'''
import random
rolls = 0
while True:
    rolls += 1
    result = random.randint(1, 6)
    
    if result == 6:
        break
print(rolls)