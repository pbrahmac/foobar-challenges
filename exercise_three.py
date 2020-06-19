def exercise3(l):
    return sorted(l, key=lambda x: tuple(map(int, x.split("."))))

if __name__ == "__main__":
    print("Exercise #3: ") 
    test3 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
    print(exercise3(test3))