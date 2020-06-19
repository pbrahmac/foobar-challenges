import math

def exercise1(area):
    # Your code here
    squaresArr = []
    def innerRecurse(a):
        if a < 1:
            return
        
        root = math.sqrt(a)

        if root == int(root):
            squaresArr.append(int(root ** 2))
            return
        
        root = math.floor(root)
        squaresArr.append(int(root ** 2))
        innerRecurse(a - (root ** 2))
    innerRecurse(area)
    return squaresArr

def exercise2(xs):
    # Your code here
    if len(xs) == 1:
        return str(xs[0])

    maxMult = 1
    negArr = [num for num in xs if num < 0]
    posArr = [num for num in xs if num > 0]
    
    if len(negArr) <= 1 and len(posArr) == 0:
        return str(0)

    negArr.sort(reverse=True)
    loopRange = 1 if len(negArr) % 2 == 1 else 0
    
    for i in range(loopRange, len(negArr)):
        maxMult *= negArr[i]
    for j in posArr:
        maxMult *= j
    
    return str(maxMult)

def exercise3(l):
    return sorted(l, key=lambda x: tuple(map(int, x.split("."))))
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def exercise4(x, y):
    counter, m, f = 0, int(x), int(y)

    if m <= 0 or f <= 0 or gcd(m, f) != 1:
        return "impossible"

    while m > 1 and f > 1:
        if m > f:
            div = m // f
            m -= div * f
        elif f > m:
            div = f // m
            f -= div * m
        counter += div

    counter += m if m > 1 else f

    return str(counter-1)

def exercise5(n):
    n, counter = int(n), 0
    while n != 1:
        if n & 1 == 0:
            n = n >> 1
        else:
            n = (n - 1) if (n - 1) & 3 == 0 or n == 3 else n + 1
        counter = (-(~counter))
    return counter

def main():
    print("Exercise #1: ")
    test1 = 15324
    print(exercise1(test1))
    print("")

    print("Exercise #2: ")
    test2 = [-2, -3, 4, -5]
    print(exercise2(test2))
    print("")

    print("Exercise #3: ") 
    test3 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    print(exercise3(test3))
    print("")

    print("Exercise #4: ") 
    testCases = [('2', '1'), ('4', '7'), ('19', '15'), ('2', '4'), ('9', '6'), ('2', str(10**50 - 1))]
    print([exercise4(case[0], case[1]) for case in testCases])
    print("")

    print("Exercise #5: ") 
    test5 = ['15', '4', '26', '100', str(2**1024)]
    print([exercise5(n) for n in test5])
    print("")

if __name__ == "__main__":
    main()