import math

def exercise_one(area):
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

if __name__ == "__main__":
    print("Exercise #1: ")
    test1 = 15324
    print(exercise_one(test1))