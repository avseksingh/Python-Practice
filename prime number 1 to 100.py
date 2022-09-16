prime = [1,2,3,]
for num in range(4, 101):
    flag = True
    for j in range(2, num):
        if num%j == 0:
           flag = False
    if flag:
        prime.append(num)
print(prime)
