# %%
'''
Homework 1 about Strings: Write a function to return a string made of the first 2 and the last 2 chars
from a given string. If the string length is 4 or less, return the entire string. For instance, it should
return unrn for unicorn and it should return abc for abc. Call that function and print its output.
'''

def solution1(string):
    new_string = ""
    if len(string) <= 4:
        return string
    else:
        new_string = string[0:2] + string[-2:]
    return new_string
print(solution1('unicorn'))
# %%
'''
Homework 2 about Strings: Write a python program to get a string as input from the user and print the
third character from the end. For instance, it should print 'o' for unicorn.
'''

def solution2(string):
    return string[4]
print(solution2(string = input("please enter a string :")))

# %%
'''
Homework 3 about Strings: Write a function that counts how many vowels are in a given string.
The function should be case-insensitive. Call the function with at least two examples.
'''
def solution3(string):
    count = 0
    for char in string.lower():
        if char in 'aeiou':
            count += 1
    return count
print(solution3('first_Example'))
print(solution3('2_Example'))


# %%
'''
Homework 4 about Strings: Write a program that receives a string from the user and prints whether
it is a palindrome or not (ignoring spaces and case).
'''
def solution4(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]
print(solution4(string=input("please any type of string to check for palindrome:")))
# %%
'''
Homework 5 about Strings: Write a function that takes two strings and returns True if one string
is an anagram of the other (ignoring spaces and case). Otherwise, return False.
'''
def solution5(string1, string2):
    s1 = string1.lower().replace(' ', '')
    s2 = string2.lower().replace(' ', '')
    return sorted(s1) == sorted(s2)

print(solution5("string", "gst inr"))

# %%
'''
Homework 6 about Strings: Write a program that receives a sentence from the user and counts the
number of words in it. Assume words are separated by spaces.
'''

def solution6(sentence):
    return len(sentence.split())
print(solution6("i guess this counts as seven words"))

# %%
'''
Homework 7 about Strings: Write a function that replaces all vowels in a string with the character '*'.
Call the function with a few examples.
'''

def solution7(string):
    for char in 'aeiouAEIOU':
        string = string.replace(char, '*')
    return string
print(solution7('example'))
print(solution7('few_example'))


# %%
'''
Homework 8 about Strings: Write a program that receives a string and prints the frequency of each character
in the string. Ignore case and spaces.
'''
from collections import Counter
def solution8(string):
    string = string.lower().replace(' ','')
    return Counter(string)
print(solution8('frequency counter'))


# %%
'''
Homework 9 about Strings: Write a program that receives a string and prints all unique characters in it
(sorted alphabetically). For example, "banana" should output 'abn'.
'''

def solution9(string):
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
    return ''.join(sorted(seen))
print(solution9("banana"))


# %%
'''
Homework 10 about Strings: Write a program that receives a string and checks if it contains at least
one digit, one uppercase letter, and one lowercase letter. Print "Valid string" if all conditions are met,
otherwise print "Invalid string".
'''

def solution10(string):
    return "Valid string" if any(c.isdigit() for c in string) and any(c.isupper() for c in string) and any(c.islower() for c in string) else 'Invalid string'
print(solution10("Axl1model"))