def is_split_possible(arr):
    odd_count = 0

    # Count the number of odd elements in the array
    for num in arr:
        if num % 2 != 0:
            odd_count += 1

    # Check if the number of odd elements is even
    if odd_count % 2 == 0:
        return True  # Split is possible
    else:
        return False  # Split is not possible

# Main program
N = int(input())
arr = list(map(int, input().split()))

if is_split_possible(arr):
    print("1")  # Split is possible
else:
    print("0")  # Split is not possible