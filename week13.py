# %%
'''
Homework 1 about Try/Except:
Write a program that asks the user to enter an integer. Use try/except to catch ValueError
if the input is not an integer, and print "Invalid input".
'''

try:
    input = int(input('enter a integer:'))
except ValueError:
    print('Invalid input')


# %%
'''
Homework 2 about Try/Except:
Write a function divide(a, b) that returns a/b. Handle ZeroDivisionError by returning
"Cannot divide by zero".
'''
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by Zero"

print(divide(3,0))



# %%
'''
Homework 3 about Try/Except:
Write a program that opens a file "sample.txt" and prints its contents.
If the file does not exist, catch FileNotFoundError and print "File not found".
'''

try:
    with open("sample.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")



# %%
'''
Homework 4 about Try/Except:
Write a program that tries to convert a list of strings ["1", "2", "three", "4"] into integers.
Use try/except to skip items that cannot be converted. Print the list of valid integers.
'''
string_list = ["1", "2", "three", "4"] 
result = []
for char in string_list:
    try:
        num = int(char)
        result.append(num)
    except ValueError:
        pass

print(result) 


# %%
'''
Homework 5 about Try/Except:
Write a program that repeatedly asks the user for a number until they enter a valid integer.
Use try/except to handle invalid inputs.
'''
while True:
    try:
        num = int(input("enter number"))
        break
    except ValueError:
        print("not a number")

# %%
'''
Homework 6 about Try/Except:
Write a function safe_dict_access(d, key) that returns d[key].
If the key does not exist, catch the KeyError and return "Key not found".
'''

def safe_dict(d, key):
    try:
        return d[key]
    except KeyError:
        return "key not found"



# %%
'''
Homework 7 about Try/Except:
Write a program that converts a string input into a float.
Handle both ValueError (invalid float) and TypeError (wrong type).
'''
str_input = input("enter a decimal values")
def convert(str_input):
    try:
        return float(str_input)
    except (ValueError, TypeError):
        return "Invalid input"

print(convert(str_input))

# %%
'''
Homework 8 about Try/Except:
Write a program that divides two numbers entered by the user.
Handle both ValueError (non-numeric input) and ZeroDivisionError.
'''
try:
    num1 = float(input("enter a number"))
    num2 = float(input("enter a number"))
    result = num1/num2
    print(result)
except ValueError:
    print("its non-numerice value")
except ZeroDivisionError:
    print("cannot divide by zero")

# %%
'''
Homework 9 about Try/Except:
Write a program that tries to open "data.txt" for reading.
If the file doesn’t exist, create the file and write "New file created".
'''

try:
    with open("data.txt", "r") as f:
        f.read()
except FileNotFoundError:
    with open("data.txt", "w") as f:
        f.write("New file created")
    



# %%
'''
Homework 10 about Try/Except:
Write a function list_average(lst) that returns the average of numbers in lst.
If lst is empty, handle ZeroDivisionError and return "List is empty".
If lst contains non-numeric values, handle TypeError or ValueError.
'''

def list_average(lst):
    try:
        return sum(lst)/len(lst)
    except ZeroDivisionError:
        return "List is empty"
    except (TypeError, ValueError):
        return "List contains non-numeric "