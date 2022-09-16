a = "geeksforgeeks"
b = "forgeeksgeeks"

if len(a) == len(b):
    for i in range(len(a) - 1):
        for e in b:
            if a[i] == b:
                a.pop(i)

print(a)