for j in range(1,6):
    for i in range(1,6):
        if i == j:
            print("*" * i, end="")
            break
        print(i, end="")
    for i in reversed(range(1,6)):
        if i == j:
            print("*" * j, end="")
            break
        print(i, end="")
    print()