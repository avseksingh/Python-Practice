a1 = "geeksforgeeks"
b1 = "forgeeksgeeks"
a = ''.join(sorted(a1))
b = ''.join(sorted(b1))
flag = False
if len(a1) == len(b1):
    for i in range(len(a)):
        if a[i] == b[i]:
            flag = True
        else:
            flag = False
            break
if flag:
    print("String is Anagram")
else:
    print("string is not an anagram")




# if len(a) == len(b):
#     for i in range(len(a) - 1):
#         for e in b:
#             if a[i] == b:
#                 a.pop()
#
# print(a)