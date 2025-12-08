# %%
'''
Homework 1 about Lists, Tuples, and Sets: Write a function that receives a tuple as input. The tuple
might include duplicates. Convert the tuple to a set which will remove duplicates automatically. Then
convert the set to a list. Then sort the list. Then create a new list that includes the items in the
previous list, each one duplicated as many times as its index. For instance, the first item in the list
would appear only once in the new list, the second item in the list would appear two times in the list, etc.
Then it returns the new list. For instance, if the input is ('b', 'a', 'c', 'a', 'c'), the output should
be ['a', 'b', 'b', 'c', 'c', 'c']. If the input is (8, 5, 6, 6), the output should be [5, 6, 6, 8, 8, 8].
'''

def solution1(tuple_input):
    converted = set(tuple_input)
    conv_list = list(converted)
    conv_list.sort()
    result = []
    for i, char in enumerate(conv_list):
        result.extend([char]*(i+1))
    return result
print(solution1(('b', 'a', 'c', 'a', 'c')))


# %%
'''
Homework 2 about Lists, Tuples, and Sets: Write a function that receives a list of integers as its
argument. The function should join individual elements of this list of integers to create a string.
Inside the string, the elements should be separated using a comma. Then return the string. For instance,
if you call the function and pass [1, 2, 3], the returned string should be "1,2,3". Please note that there
is no space around the comma in the string. Please note that the join function only operates on
lists whose elements are string. Since your list includes integers in this case, you need to take an
extra step to make it possible to use the join function.
'''

def solution2(integers_input):
    new_string = ','.join(str(x) for x in integers_input)
    return f'"{new_string}"'
print(solution2([1,2,3]))

# %%
'''
Homework 3 about Lists, Tuples, and Sets: Write a function that receives a tuple of integers
and returns a new tuple containing only the even numbers from it.
For example, if the input is (1, 2, 3, 4, 5, 6), the output should be (2, 4, 6).
'''

def solution3(tuple_input):
    conv_list = list(tuple_input)
    result = []
    for num in conv_list:
        if num % 2 == 0:
            result.append(num)
    return tuple(result)
print(solution3((1,2,3,4,5,6)))



# %%
'''
Homework 4 about Lists, Tuples, and Sets: Write a function to flatten a list by one nesting level.
It should take a list whose elements may include lists/tuples/sets and return a single flat list.
Example: [1, [2, 3], (4, 5), {6, 7}] -> [1, 2, 3, 4, 5, 6, 7].
'''

def solution4(input_list):
    result = []
    for items in input_list:
        if isinstance(items, (list, tuple, set)):
            result.extend(items)
        else:
            result.append(items)
    return result        

print(solution4(input_list=[1, [2, 3], (4, 5), {6, 7}]))

# %%
'''
Homework 5 about Lists, Tuples, and Sets: Given a tuple t, return a new tuple in which the first occurrence
of the minimum value and the first occurrence of the maximum value are swapped. All other elements remain
in their original positions. Example: (3, 1, 4, 1, 5) -> (3, 5, 4, 1, 1).
'''

def solution5(tuple_input):
    conv_list = list(tuple_input)
    min_val = min(conv_list)
    max_val = max(conv_list)

    min_idx = conv_list.index(min_val)
    max_idx = conv_list.index(max_val)

    conv_list[min_idx], conv_list[max_idx] = conv_list[max_idx], conv_list[min_idx]
    return tuple(conv_list)
print(solution5((3,1,4,1,5)))






# %%
'''
Homework 6 about Lists, Tuples, and Sets: Write a function that takes two lists and returns:
(1) the sorted list of unique elements in their intersection, and
(2) the sorted list of unique elements in their symmetric difference.
Use set operations, then convert to lists and sort before returning.
'''

def solution6(first_list, second_list):
    set1 = set(first_list)
    set2 = set(second_list)

    intersection_list = sorted(list(set1 & set2))
    symmetric_difference = sorted(list(set1 ^ set2))
    return (intersection_list, symmetric_difference)

print(solution6([10, 20, 30, 40, 50, 60], [60, 70, 80, 90, 100]))



# %%
'''
Homework 7 about Lists, Tuples, and Sets: Remove duplicates from a list while preserving the order
of first occurrence. Return the deduplicated list. Example: [3,1,3,2,1] -> [3,1,2].
'''

def solution7(input_list):
    seen = set()
    result = []
    for num in input_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(solution7([3,1,3,2,1]))

# %%
'''
Homework 8 about Lists, Tuples, and Sets: Compute the moving average of a list of numbers given a window size k.
Return a list of floats of length len(nums) - k + 1 where each element is the average of a window.
Raise ValueError if k <= 0 or k > len(nums).
'''

def solution8(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("dont work")
    result = []
    for i in range(len(nums)-k+1):
        curr_sum = sum(nums[i:i+k])
        result.append(curr_sum/k)
    return result

print(solution8([1,2,3,4,5,6,7], 3))
# %%
'''
Homework 9 about Lists, Tuples, and Sets: Given a list, return a list of (item, count) tuples sorted by
descending count then ascending item. Use Counter from collections for counting.
'''
from collections import Counter

def solution9(input_list):
    frequency = Counter(input_list)
    return sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
print(solution9(['b', 'a', 'a', 'c', 'b', 'b', 'c', 'a']))
# %%
'''
Homework 10 about Lists, Tuples, and Sets: Given a list of (name, score) pairs, normalize scores to the [0, 1]
range using (x - min) / (max - min). If all scores are equal, return 0.0 for all. Return a new list of tuples.
Example: [("Ann", 50), ("Bob", 80), ("Cia", 80)] -> [("Ann", 0.0), ("Bob", 1.0), ("Cia", 1.0)].
'''

def solution10(input_list):
    scores = [score for _, score in input_list]
    min_score = min(scores)
    max_score = max(scores)

    result = []
    score_range = max_score - min_score
    for name, score in input_list:
        curr_Sum = (score - min_score)/score_range
        result.append((name, curr_Sum))
    return result
        
data1 = [("Ann", 50), ("Bob", 80), ("Cia", 80), ("Dave", 65)]
print(solution10(data1))

# %%
