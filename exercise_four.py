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

    return str(counter - 1)

if __name__ == "__main__":
    print("Exercise #4: ") 
    testCases = [('2', '1'), ('4', '7'), ('19', '15'), ('2', '4'), ('9', '6'), ('2', str(10**50 - 1))]
    print([exercise4(case[0], case[1]) for case in testCases])