class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

def user_logic(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return 1  # Single node is always a valid pattern

    # Convert linked list to an array for easy processing
    nums = []
    current = linked_list.head
    while current:
        nums.append(current.data)
        current = current.next

    last_significant_number_index = 0  # Track last distinct number index

    for i in range(1, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            continue  # Skip duplicate values

        # Check if it's a hill (local peak) or a valley (local dip)
        if (nums[i] > nums[last_significant_number_index] and nums[i] > nums[i + 1]) or \
           (nums[i] < nums[last_significant_number_index] and nums[i] < nums[i + 1]):
            last_significant_number_index = i  # Update last significant index
        else:
            return 0  # Pattern breaks

    return 1  # If pattern holds, return 1

    
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    values = list(map(int, data[1:]))
    ll = LinkedList()
    for value in values:
        ll.push(value)
    result = user_logic(ll)
    print(result)

if __name__ == "__main__":
    main()