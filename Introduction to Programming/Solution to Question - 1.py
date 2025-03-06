# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

count = 0  # To count prime numbers found
num = 1    # Start checking from 2

while count < n:
    num += 1
    is_prime = True

    # Check if num is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        count += 1  # Increase count if prime

print(f"{num**2}")