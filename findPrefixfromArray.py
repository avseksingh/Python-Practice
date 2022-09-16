a = ["GEEK", "GEEKSS", "GEEKSFORGEE"]
a.sort()
str1 =a[0] #"GEEKans"
str2 =a[len(a)-1] #"GEEKS"
n1 = len(str1)
n2 = len(str2)
n = min(n1, n2)
prefix = ""
i = 0
while i <= n - 1 and str1[i] == str2[i]:
    i += 1
prefix = str1[:i]
print(prefix)
