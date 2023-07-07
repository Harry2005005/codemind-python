def min_operations(N, A):
    odd_count = 0

    # Count the number of characters with odd occurrences
    for count in A:
        if count % 2 != 0:
            odd_count += 1

    # Minimum operations required is the number of characters with odd occurrences divided by 2
    return odd_count // 2

# Main program
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    min_ops = min_operations(N, A)
    print(min_ops)