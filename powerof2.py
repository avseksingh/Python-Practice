# Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2x for some x.

def isPowerofTwo(self, n):
    ##Your code here
    if n == 0:
        print("False")
    n = n & (n - 1)
    print(n)
    return n == 0

isPowerofTwo(int(input("Enter Value : ")),5)


# class Solution:
#     # Function to rotate an array by d elements in counter-clockwise direction.
#     def rotateArr(self, a, d, n):
#         # Your code here
#         for i in range(d):
#             a.append(a.pop(0))
#
#         print(a)