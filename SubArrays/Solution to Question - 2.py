import sys
input = sys.stdin.read

def countValidPartitions(E, N):
    # User logic goes here
    if N < 3:
        return 0  # Cannot form three zones if size < 3

    prefix_sum = [0] * (N + 1)

    # Step 1: Compute Prefix Sum
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + E[i]

    valid_count = 0

    # Step 2: Iterate Over Possible Alpha Sizes
    for size in range(1, N // 2 + 1):
        if N - 2 * size <= 0:  # Ensure there is space for Beta
            break

        sum_alpha = prefix_sum[size]  # Sum of Alpha (First 'size' elements)
        sum_gamma = prefix_sum[N] - prefix_sum[N - size]  # Sum of Gamma (Last 'size' elements)
        sum_beta = prefix_sum[N - size] - prefix_sum[size]  # Middle section (Beta)

        # Check if Alpha + Gamma > Beta
        if sum_alpha + sum_gamma > sum_beta:
            valid_count += 1

    return valid_count # Placeholder return value

if __name__ == "__main__":
    data = input().split()
    N = int(data[0])
    E = list(map(int, data[1:]))
    result = countValidPartitions(E, N)
    print(result)
