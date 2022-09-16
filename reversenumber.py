n = 123
rem = 0
rev = 0
while n:
    rem = n%10
    rev = rev *10 + rem
    n //= 10
print(rev)
