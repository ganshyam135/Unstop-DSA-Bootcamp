def validate_password(password):
    """
    Function to validate the password based on given conditions.
    Parameters:
        password (list): List of integers representing the password elements.
    Returns:
        tuple: A tuple containing a string ("VALID" or "INVALID") and an integer (the most frequent element).
    """
    # Manually count occurrences of each number
    frequency = {}
    for num in password:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Check if all numbers have even occurrences
    all_even = True
    has_exactly_two = False

    for count in frequency.values():
        if count % 2 != 0:
            all_even = False
        if count == 2:
            has_exactly_two = True

    # Find the most frequent element (if tied, pick the smallest one)
    max_frequency = -1
    most_frequent = None

    for num in frequency:
        if frequency[num] > max_frequency or (frequency[num] == max_frequency and num < most_frequent):
            max_frequency = frequency[num]
            most_frequent = num

    # Determine if the password is VALID or INVALID
    if all_even and has_exactly_two:
        return "VALID", most_frequent
    else:
        return "INVALID", most_frequent


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    password = list(map(int, data[1:]))  # Remaining input is the password array
    
    # Call user logic function
    validation_result, most_frequent_element = validate_password(password)
    
    # Print the output
    print(validation_result)
    print(most_frequent_element)

if __name__ == "__main__":
    main()