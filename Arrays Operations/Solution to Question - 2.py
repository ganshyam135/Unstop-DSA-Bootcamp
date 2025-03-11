def calculate_wish_values_sum(N, A):
    """
    Compute the sum of all wish values.
    Parameters:
        N (int): Number of mountain peaks
        A (list): List of brightness values of each peak
    Returns:
        int: Sum of all wish values
    """
    max_right = [0] * N
    min_left = [0] * N

    # Compute max_right array
    max_right[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        max_right[i] = max(A[i], max_right[i + 1])

    # Compute min_left array
    min_left[0] = A[0]
    for i in range(1, N):
        min_left[i] = min(A[i], min_left[i - 1])

    # Compute the sum of wish values
    wish_sum = 0
    for i in range(N):
        wish_sum += abs(max_right[i] - min_left[i])

    return wish_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    A = list(map(int, data[1:]))  # Remaining input is the array of integers representing brightness values
    
    # Call user logic function and print the output
    result = calculate_wish_values_sum(N, A)
    print(result)

if __name__ == "__main__":
    main()