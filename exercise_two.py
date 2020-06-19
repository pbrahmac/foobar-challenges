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

if __name__ == "__main__":
    print("Exercise #2: ")
    test2 = [-2, -3, 4, -5]
    print(exercise2(test2))