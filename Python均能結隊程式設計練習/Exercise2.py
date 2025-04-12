def patternA(n):
    print("Pattern A")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

def patternB(n):
    print("Pattern B")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

def patternC(n):
    print("Pattern C")
    for i in range(1, n + 1):
        print("  " * (n - i), end='') 
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()

def patternD(n):
    print("Pattern D")
    for i in range(n, 0, -1):
        print("  " * (n - i), end='') 
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# 執行程式
n = 6  
patternA(n)
print()
patternB(n)
print()
patternC(n)
print()
patternD(n)