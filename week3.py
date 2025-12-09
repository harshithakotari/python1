# %%
'''
Homework 1 about Functions: Write a function that receives two numbers as parameters and returns their
multiplication. Call that function and print its output. For instance, if the arguments are 3 and 5,
the output should be 15.
'''

def solution1(a, b):
    return a*b
print(solution1(3, 5))


# %%
'''
Homework 2 about Functions: Write a function that receives three parameters: name, weight, and height.
The default value for name is James. The function calculates the BMI. BMI is: weight/(height^2).
Weight should be in kg and height should be in meters. For instance, if the weight is 60 kg and the
height is 1.7 m, then the BMI should be 20.76. The function should return "<name>'s BMI is greater
than or equal to 22" if the BMI is greater than or equal to 22. Otherwise, return "<name>'s BMI is less than 22".
Call the function and print its output.
'''
def solution2(weight, height, name='James'):
    bmi = weight/(height**2)
    if bmi >= 22:
        return f"{name}'s BMI is greater than or equal to 22"
    else:
        return f"{name}'s BMI is less than 22"
print(solution2(60, 1.7))
    

# %%
'''
Homework 3 about Functions: Write a function that receives a string as input and returns the number of vowels in it.
Call the function and print the result for at least two sample strings.
'''

def solution3(string):
    count = 0
    for char in string:
        if char in 'aeiou':
            count += 1
    return count
print(solution3('sample_string'))
print(solution3('another_sample_string'))

# %%
'''
Homework 4 about Functions: Write a function that receives an integer n and returns the factorial of n.
Call the function for n = 5 and n = 7 and print the results.
'''

def solution4(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result
print(solution4(5))
print(solution4(7))

# %%
'''
Homework 5 about Functions: Write a function that receives a list of numbers and returns the maximum and minimum values.
Call the function with a sample list and print the results.
'''

def solution5(nums):
    return [max(nums), min(nums)]
nums = [5, 6,1,7,4,3,9, 10, 15]
print(solution5(nums))


# %%
'''
Homework 6 about Functions: Write a function that takes a list of numbers and returns a new list with only the even numbers.
Call the function and print the returned list.
'''

def solution6(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result

nums = [1,2,3,4,5,6,7,8,9,10]
print(solution6(nums))



# %%
'''
Homework 7 about Functions: Write a recursive function that calculates the nth Fibonacci number.
Call the function for n = 5 and n = 10 and print the results.
'''

def solution7(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return solution7(n-1) + solution7(n-2)
print(solution7(5))
print(solution7(10))


# %%
'''
Homework 8 about Functions: Write a function that accepts any number of integer arguments (*args)
and returns their average. Call the function with 3, 5, 7 and with 10, 20, 30, 40.
'''

def solution8(*args):
    if not args:
        return 0
    return sum(args)/len(args)
print(solution8(3,5,7))
print(solution8(10,20, 30, 40))



# %%
'''
Homework 9 about Functions: Write a function that accepts a dictionary of student names and their scores.
The function should return the name of the student with the highest score.
'''

def solution9(reports):
    max_score = float('-inf')
    student_name = ""
    for name, score in reports.items():
        if score > max_score:
            max_score = score 
            student_name = name
    return student_name

student_reports = {
    'Alice': 88, 
    'Bob': 91, 
    'Charlie': 90, 
    'David': 95
}
print(solution9(student_reports))
# %%
'''
Homework 10 about Functions: Write a function that checks if a given string is a palindrome (the same forwards and backwards).
Call the function with at least two examples and print the results.
'''

def solution10(string):
    return True if string == string[::-1] else False
print(solution10('ABCCBA'))
print(solution10('okay'))
