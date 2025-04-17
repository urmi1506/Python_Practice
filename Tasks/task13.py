# Fibonacci Series

def fibonacci():
    n1 = 0
    n2 = 1
    print(n1, n2, end=' ')
    
    for _ in range(8):  
        n3 = n1 + n2
        print(n3, end=' ')
        n1 = n2
        n2 = n3

fibonacci()

