n = int(input())

# Iterate from 1 to n
for i in range(1, n+1):
    
    print(" " * (n - i), end='')
    
    
    for j in range(1, i+1):
        print(j, end='')
    
    for j in range(i-1, 0, -1):
        print(j, end='')
    
    print()  