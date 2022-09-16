a = [1,2,3,4,2,4,5,3,2,4]
n = len(a)-1
a.sort()
print(a)
for l1 in range(0,n):
    if a[l1] > a[l1 - 1]:
        for l2 in range(l1+1, n):
            if a[l1] == a[l2]:
                print(a[l1])
                break


