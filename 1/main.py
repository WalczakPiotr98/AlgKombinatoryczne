# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


def maxelement(arr):
    no_of_rows = len(arr)
    no_of_column = len(arr[0])
    for i in range(no_of_rows):
        max1 = 0
        for j in range(no_of_column):
            if arr[i][j] > max1:
                max1 = arr[i][j]
        return max1


def ret_i(arr):
    k = 0
    no_of_rows = len(arr)
    no_of_column = len(arr[0])
    for i in range(no_of_rows):
        max1 = 0
        for j in range(no_of_column):
            if arr[i][j] > max1:
                max1 = arr[i][j]
                k = i
        return k


def ret_j(arr):
    no_of_rows = len(arr)
    no_of_column = len(arr[0])
    k = 0
    for i in range(no_of_rows):
        max1 = 0
        for j in range(no_of_column):
            if arr[i][j] > max1:
                max1 = arr[i][j]
                k = j
        return k


A = np.random.randint(-5, 5, size=(5, 5))
print(A)
g1 = 0
g2 = 0
for k in range(len(A)):
    if g1 == g2:
        g1 = g1 + maxelement(A)
        A = np.delete(A, ret_i(A), 1)
        A = np.delete(A, ret_j(A), 0)
        print(A)
    elif g2 < g1:
        g2 = g2 + maxelement(A)
        A = np.delete(A, ret_i(A), 1)
        A = np.delete(A, ret_j(A), 0)
        print(A)
    elif g2 > g1:
        g1 = g1 + maxelement(A)
        A = np.delete(A, ret_i(A), 1)
        A = np.delete(A, ret_j(A), 0)
        print(A)
print("g1 ", g1)
print("g2 ", g2)