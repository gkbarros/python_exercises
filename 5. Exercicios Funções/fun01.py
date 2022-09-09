def print_n(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


n = int(input('Type a num: '))
print_n(n)
