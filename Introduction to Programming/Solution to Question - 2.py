def count_brave_soldiers(n):
    """
    Write your logic here.
    Parameters:
        n (int): The number of soldiers in the army
    Returns:
        int: The count of brave soldiers
    """
    count=0
    for num in range(2,n+1):
        is_brave=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_brave=False
                break
        if is_brave:
            count+=1
    return count

    

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())  # The input contains only one integer N
    
    # Call the user logic function and print the output
    result = count_brave_soldiers(n)
    print(result)

if __name__ == "__main__":
    main()