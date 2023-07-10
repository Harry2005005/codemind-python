n = int(input())

# Iterate from 1 to n
for i in range(1, n+1):
    # Print the numbers
    for j in range(i, n+1):
        print(j, end=' ')
    
    print()  # Move to the next line