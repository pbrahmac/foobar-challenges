def exercise5(n):
    n, counter = int(n), 0
    while n != 1:
        if n & 1 == 0:
            n = n >> 1
        else:
            n = (n - 1) if (n - 1) & 3 == 0 or n == 3 else n + 1
        counter = (-(~counter))
    return counter

if __name__ == "__main__":
    print("Exercise #5: ") 
    test5 = ['15', '4', '26', '100', str(2**1024)]
    print([exercise5(n) for n in test5])