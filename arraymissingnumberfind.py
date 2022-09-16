# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
n = 5
arr = {1,2,3,5}
val = 0
for i in range(1,n+1):
    val +=i
    result = val - sum(arr)
print(result)