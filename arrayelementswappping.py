class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, a, d, n):
        # Your code here
        for i in range(d):
            a.append(a.pop(0))

        print(a)