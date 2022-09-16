a = "shaktiman"
list = []
f= 1
for ch in a:
    if ch in list:
        f= 0
        print(ch)
        break
    list.append(ch)
if f:
    print("No any repeated character")
