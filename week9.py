# %%
'''
Homework 1 about Dictionaries: Write a function that receives a dictionary and a variable as its arguments and
returns True if that variable exists among the values of the dictionary and False if it does not.
For instance, if dict={'name': 'John', 'expertise': 'Math'} and variable='John', then your function should return True.
If dict={'name': 'John', 'expertise': 'Math'} and variable='name', then your function should return False.
'''
def solution1(input, variable):
    return variable in input.values()
print(solution1({'name': 'John', 'expertise': 'Math'}, 'John')) 

# %%
'''
Homework 2 about Dictionaries: Write a function that receives a dictionary as input and returns the key
for the minimum value among the dictionary values. Call that function and print its output. You can test
your function with {'Math': 25, 'History': 20, 'Physics': 18, 'Geography': 19} and it should return Physics.
'''
def solution2(input):
    return min(input, key=input.get)
print(solution2({'Math': 25, 'History': 20, 'Physics': 18, 'Geography': 19}))
# %%
'''
Homework 3 about Dictionaries: Write a function that receives a dictionary of student names as keys and their scores
as values, and returns the average score of the class. For example, if the input is {'Alice': 80, 'Bob': 90, 'Charlie': 70},
the output should be 80.0.
'''

def solution3(input):
    return sum(score for _, score in input.items())/len(input)
print(solution3({'Alice': 80, 'Bob': 90, 'Charlie': 70}))
# %%
'''
Homework 4 about Dictionaries: Write a function that receives a dictionary and returns a new dictionary with
the keys and values swapped. For example, if the input is {'a': 1, 'b': 2, 'c': 3}, the output should be {1: 'a', 2: 'b', 3: 'c'}.
'''
def solution4(input):
    new_dict = {}
    for char, val in input.items():
        new_dict[val] = char
    return new_dict
print(solution4({'a': 1, 'b': 2, 'c': 3}))
# %%
'''
Homework 5 about Dictionaries: Write a function that receives a dictionary and a key as input,
and removes that key-value pair from the dictionary if it exists. Return the updated dictionary.
For example, if the input is {'x': 10, 'y': 20, 'z': 30} and key='y', the output should be {'x': 10, 'z': 30}.
'''

def solution5(input, key):
    if key in input:
        del input[key]
    return input
print(solution5({'x': 10, 'y': 20, 'z': 30}, 'y'))


# %%
'''
Homework 6 about Dictionaries: Write a function that receives two dictionaries and merges them into one.
If the same key exists in both, the value from the second dictionary should overwrite the first.
For example, if dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c': 4}, the output should be {'a': 1, 'b': 3, 'c': 4}.
'''

def solution6(dict1, dict2):
    return dict1 | dict2
print(solution6({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

# %%
'''
Homework 7 about Dictionaries: Write a function that receives a string and returns a dictionary
where each key is a word and its value is the number of times that word appears in the string.
For example, if the input is "apple banana apple orange banana", the output should be
{'apple': 2, 'banana': 2, 'orange': 1}.
'''

def solution7(sentence):
    words = sentence.lower().split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(solution7("apple banana apple orange banana"))

# %%
'''
Homework 8 about Dictionaries: Write a function that receives a dictionary of items and their prices,
and returns the item with the highest price. For example, if the input is {'apple': 2.5, 'banana': 1.2, 'milk': 3.0},
the output should be 'milk'.
'''

def solution8(input):
    return max(input, key=input.get)
print(solution8({'apple': 2.5, 'banana': 1.2, 'milk': 3.0}))
    

# %%
'''
Homework 9 about Dictionaries: Write a function that receives a dictionary of numbers as keys and their squares as values,
and returns True if all values are correct squares of the keys, otherwise returns False.
For example, if the input is {2: 4, 3: 9, 4: 16}, the output should be True. If the input is {2: 5, 3: 9}, the output should be False.
'''

def solution9(input):
    for key, val in input.items():
        if val != key*key:
            return False
    return True
print(solution9({2: 4, 3: 9, 4: 16}))
print(solution9({2: 5, 3: 9}))
# %%
'''
Homework 10 about Dictionaries: Write a function that receives a dictionary where the values are lists of integers,
and returns a dictionary with the same keys but where each list is replaced by its maximum value.
For example, if the input is {'a': [1, 2, 3], 'b': [5, 0], 'c': [10]}, the output should be {'a': 3, 'b': 5, 'c': 10}.
'''
def solution10(input):
    for key, val in input.items():
        input[key] = max(val)
    return input
print(solution10({'a': [1, 2, 3], 'b': [5, 0], 'c': [10]}))