# %%
'''
Extract 'make' and 'price' columns from the full automobile CSV file.
Clean the data by removing rows with missing price ('?').
Convert price to numeric and save the cleaned output to a new CSV file.
'''
import pandas as pd
# Step 1: Load full CSV file
df = pd.read_csv("Automobile_data.csv")  # replace with actual path if needed
# Step 2: Extract only 'make' and 'price' columns
df_make_price = df[['make', 'price']]
# Step 3: Filter out rows with missing price
df_make_price = df_make_price[df_make_price['price'] != '?']
# Step 4: Convert price to numeric
df_make_price['price'] = pd.to_numeric(df_make_price['price'])
# Step 5: Save new CSV file
df_make_price.to_csv("make_price_cleaned.csv", index=False)
print("new CSV saved as 'make_price_cleaned.csv'")

# %%
'''
Homework 0 about Libraries: NumPy stands for Numerical Python. This Python library provides support for
large multidimensional array objects and various tools to work with them. The difference between Python
lists and NumPy arrays: Lists contain elements with different data types, but NumPy arrays contain only
homogeneous elements, i.e. elements having the same data type. This makes it more efficient at storing
and manipulating the array. This difference becomes apparent when the array has a large number of elements,
say thousands or millions. Also, with NumPy arrays, you can perform element-wise operations, something
which is not possible using Python lists! This is the reason why NumPy arrays are preferred over Python
lists when performing mathematical operations on a large amount of data. Write a program to delete the
second column from the following array and insert the following new column in its place, and print the result.
original_array = numpy.array(
[[34 43 73]
[82 22 12]
[53 94 66]])
new_column = numpy.array([[10,10,10]])
After insertion, your array should look like:
[[34 10 73]
[82 10 12]
[53 10 66]]
'''
import numpy as np
original_array = np.array(
[[34, 43, 73],
[82, 22, 12],
[53, 94, 66]])

new_col = np.array([[10,10,10]])
original_array[:,1] = new_col
print(original_array)


# %%
'''
Homework 1 about Libraries: Pandas is a Python library for data manipulation and analysis. 
Download this CSV file and take a look at it. Use pandas library to read this file as a data frame. 
Write a program to find the name of the company that has the most expensive car. 
Print out the name of this company. The correct output is mercedes-benz.
'''

import pandas as pd

df = pd.read_csv("Automobile_data.csv")
df['price'] = pd.to_numeric(df['price'], errors='coerce')
max_price = df['price'].idmax()
expensive_car = df.loc[max_price, 'make']
print('expensive_car')


# %%
'''
Homework 2 about Libraries: Use the math library to compute the greatest common divisor (GCD) 
of two integers input by the user.
'''

import math

num1 = input('Enter')
num2 = input('enter')
result = math.gcd(int(num1), int(num2))
print(result)

# %%
'''
Homework 3 about Libraries: Use the random library to generate a random password of length 10. 
The password should contain uppercase letters, lowercase letters, digits, and symbols.
'''

import random, string

all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
password = "".join(random.choice(all_chars) for _ in range(10))
print(password)

# %%
'''
Homework 4 about Libraries: Use numpy to create a 5x5 matrix of random integers between 1 and 50. 
Then compute the row sums and column sums.
'''

matrix = np.random.randint(1, 51, size=(5,5))
row_sum = matrix.sum(axis=1)
col_sum = matrix.sum(axis=0)
print(row_sum, col_sum)

# %%
'''
Homework 5 about Libraries: Use datetime to calculate the number of days between 
two given dates: July 4, 2020 and September 6, 2025.
'''

from datetime import date

date1 = date(2020, 7, 4)
date2 = date(2025, 9, 6)
gap = date2 - date1
days = gap.days
print(days)

# %%
'''
Homework 6 about Modules: Write a module named "math_utils.py" with a function power(base, exp) 
that returns base raised to exp. Import this module and test it with 2^5.
'''

from math_utils import power

result = power(2, 5)
print(result)

# %%
'''
Homework 7 about Modules: Write a module named "greetings.py" with a function hello(name) 
that prints "Hello, <name>!". Import and test it.
'''

from greetings import hello

hello("world")

# %%
'''
Homework 8 about Modules: Write a module named "geometry.py" with functions area_rectangle(l, w) 
and perimeter_rectangle(l, w). Import the module and test both functions.
'''

from geometry import area_rectangle, perimeter_rectangle

print(area_rectangle(10, 4))
print(perimeter_rectangle(10,4))


# %%
'''
Homework 9 about Modules: Write a module named "text_utils.py" with a function word_count(s) 
that returns the number of words in a string. Import it and test it.
'''

from text_utils import word_count

print(word_count("Testing it works given length of words"))

# %%
'''
Homework 10 about Modules: Write a module named "stats_utils.py" with a function median(lst) 
that returns the median of a list of numbers without using statistics library. 
Import and test it with [7, 1, 3, 5].
'''

from stats_utils import median

print(median([7,1,3,5]))