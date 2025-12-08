# %%
'''
Homework 1 about Lists, Tuples, and Sets: Write a function that receives a list of integers and returns
that list after removing prime numbers from the list. The number one is not a prime number. Test your
function with multiple lists of numbers and make sure it works properly. For instance, if the input
is [1, 2, 3, 4, 5, 6, 7], it should return [1, 4, 6].
'''

def solution1(nums):
    result = []
    for num in nums:
        if num <= 1:
            result.append(num)
            continue
        is_prime = False
        for i  in range(2, num):
            if num % i == 0:
                is_prime = True
                break
        if is_prime:
            result.append(num)
    return result
print(solution1([1,2,3,4,5,6,7]))

# %%
'''
Homework 2 about Lists, Tuples, and Sets: Write a function that receives a tuple of integers
and returns the maximum and minimum values as a tuple (max, min).
For example, if the input is (4, 7, 2, 9, 1), the output should be (9, 1).
'''

def solution2(nums):
    return (max(nums), min(nums))
print(solution2((4,7,2,9,1)))

# %%
'''
Homework 3 about Lists, Tuples, and Sets: Write a function that receives two sets of integers
and returns their union, intersection, and difference as a tuple of three sets.
For example, if set1 = {1, 2, 3} and set2 = {2, 3, 4}, the output should be
({1, 2, 3, 4}, {2, 3}, {1}).
'''

def solution3(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    return (union, intersection, difference)
print(solution3({1,2,3}, {2,3,4}))

# %%
'''
Homework 4 about Lists, Tuples, and Sets: Write a function that receives a list of strings
and returns a new list with all duplicates removed, while preserving the order of first appearance.
For example, if the input is ["apple", "banana", "apple", "cherry"], the output should be
["apple", "banana", "cherry"].
'''
def solution4(str_input):
    result = []
    seen = set()
    for word in str_input:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result
print(solution4(["apple", "banana", "apple", "cherry"]))


# %%
'''
Homework 5 about Lists, Tuples, and Sets: Write a function that receives a list of integers
and returns a tuple (even_count, odd_count) representing how many even and odd numbers are in the list.
For example, if the input is [1, 2, 3, 4, 5, 6], the output should be (3, 3).
'''

def solution5(nums):
    n = len(nums)
    count = 0
    for num in nums:
        if num%2 == 0:
            count += 1
    return tuple((count, n-count))
print(solution5([1, 2, 3, 4, 5, 6]))


# %%
'''
Homework 6 about Dictionaries: Write a function called func_dict(list1, list2) that receives two lists of the same
length as its arguments, creates a dictionary called dict whose keys are items from list_1 and whose values are items
from list_2, and returns the dict. For instance, if list_1 = ['Ten', 'Twenty', 'Thirty'] and list_2 = [10, 20, 30],
then your function should return {'Ten': 10, 'Twenty': 20, 'Thirty': 30}.
'''

def func_dict(list1, list2):
    return dict(zip(list1, list2))
print(func_dict(['Ten', 'Twenty', 'Thirty'], [10, 20, 30]))


# %%
'''
Homework 7 about Dictionaries: Write a function that receives a dictionary of student names as keys
and their scores as values, and returns the name of the student with the highest score.
For example, if the input is {'Alice': 85, 'Bob': 92, 'Charlie': 78}, the output should be 'Bob'.
'''

def solution7(scores):
    return max(scores, key=scores.get)
    
print(solution7({'Alice': 85, 'Bob': 92, 'Charlie': 78}))

# %%
'''
Homework 8 about Dictionaries: Write a function that receives a string and returns a dictionary
where the keys are the characters of the string and the values are the number of times each character appears.
For example, if the input is "banana", the output should be {'b': 1, 'a': 3, 'n': 2}.
'''

def solution8(string_input):
    dict_ = {}
    for char in string_input:
        if char not in dict_:
            dict_[char] = 1
        else:
            dict_[char] += 1
    return dict_
print(solution8("banana"))
    


# %%
'''
Homework 9 about Dictionaries: Write a function that receives a dictionary with items and prices,
and returns the total price of all items.
For example, if the input is {'apple': 2.5, 'banana': 1.2, 'milk': 3.0}, the output should be 6.7.
'''

def solution9(groc_list):
    return sum(prices for items , prices in groc_list.items())
print(solution9({'apple': 2.5, 'banana': 1.2, 'milk': 3.0}))

# %%
'''
Homework 10 about Dictionaries: Write a function that receives two dictionaries and merges them into
one dictionary. If a key exists in both, the value from the second dictionary should be used.
For example, if dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c': 4},
the output should be {'a': 1, 'b': 3, 'c': 4}.
'''

def solution10(dict1, dict2):
    return dict1|dict2
print(solution10({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))


# %%
