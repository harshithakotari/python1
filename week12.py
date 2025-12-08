# %%
# Homework 1 about Problem Solving:
# Introduction: A magic square is a 2D matrix composed of n^2 integers where n is the length of one row or column.
# In a magic square each row, each column, and the two diagonals must sum to the same value.
# Problem: Given a 2D matrix, your program must determine if the square is magic or not magic. It will print
# "True" or "False" accordingly.
# Input: Your program will first take an input n, representing the length of one row of the matrix from the user.
# It will then take n lines of input containing n integers separated by spaces from the user.
'''Sample Input:
3
2 2 2
2 2 2
2 2 2
Output: "True"

Input:
3
2 7 6
9 5 1
4 3 8
Output: "True"

Input:
4
16 2 3 13
5 11 10 8
9 7 6 12
4 14 15 1
Output: "True"

Input:
4
12 3 4 5
5 67 8 9
102 3 4 6
34 2 89 0
Output: "False"
'''


n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

tar = sum(matrix[0])

for r in matrix:
    if sum(r) != tar:
        print("False")
        exit()

for c in range(n):
    if sum(matrix[r][c] for r in range(n)) != tar:
        print("False")
        exit()

if sum(matrix[i][i] for i in range(n)) != tar:
    print("False")
    exit()

if sum(matrix[i][n-1-i] for i in range(n)) != tar:
    print("False")
    exit()
print("True")