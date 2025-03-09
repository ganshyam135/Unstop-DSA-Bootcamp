def find_largest_number(arr):
    # Write your logic here
    arr.sort()  # Sorting in ascending order

    # The two smallest numbers
    smallest = arr[0]
    second_smallest = arr[1]

    # Form the largest number using them
    return int(str(second_smallest) + str(smallest))  # Placeholder return value

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_largest_number(arr)
    print(result)