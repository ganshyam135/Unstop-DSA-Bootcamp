def user_logic(n1, flowers, n2, herbs):
    # Step 1: Count the quantities of herbs in Rose's garden
    herb_count = {}
    for herb in herbs:
        if herb in herb_count:
            herb_count[herb] += 1
        else:
            herb_count[herb] = 1

    # Step 2: Compare quantities and collect flowers
    result = []
    for flower in flowers:
        if flower not in herb_count or flowers.count(flower) > herb_count[flower]:
            result.append(flower)

    # Step 3: Return result
    return result if result else [-1]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n1 = int(data[0])
    flowers = list(map(int, data[1:n1+1]))
    n2 = int(data[n1+1])
    herbs = list(map(int, data[n1+2:n1+2+n2]))
    
    # Call user logic function and get the result
    result = user_logic(n1, flowers, n2, herbs)
    
    # Print the result in the required format
    if result == [-1]:
        print(-1)
    else:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()