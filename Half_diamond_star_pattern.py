def printPattern(n):
    # Print the upper half of the diamond pattern
    for i in range(1, n):
        print('*' * i)

    # Print the lower half of the diamond pattern
    for i in range(n, 0, -1):
        print('*' * i)

n = int(input())

if n >= 3 and n <= 100:
    printPattern(n)
else:
    print("The pattern is not possible")