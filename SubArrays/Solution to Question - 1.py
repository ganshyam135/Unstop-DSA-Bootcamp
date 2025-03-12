def count_tribonacci_subarrays(n, arr):
    # Step 1: Compute Tribonacci numbers up to 10^5
    MODULO = 10**9 + 7
    tribonacci_set = set()
    a, b, c = 0, 1, 1
    while a <= 10**5:
        tribonacci_set.add(a)
        a, b, c = b, c, (a + b + c) % MODULO  # Compute next Tribonacci

    # Step 2: Count valid subarrays
    count = 0
    start = 0  # Marks the start of a valid sequence

    while start < n:
        if arr[start] not in tribonacci_set:
            start += 1
            continue

        end = start
        while end < n and arr[end] in tribonacci_set:
            end += 1

        length = end - start
        count += (length * (length + 1)) // 2  # Sum of 1 to length

        start = end  # Move to next potential valid subarray

    return count % MODULO  # Return the count with modulo

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:n+1]))  # Next N inputs are the array elements
    
    # Call user logic function and print the output
    result = count_tribonacci_subarrays(n, arr)
    print(result)

if __name__ == "__main__":
    main()