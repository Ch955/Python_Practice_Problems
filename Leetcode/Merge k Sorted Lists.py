class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    
values = list(map(int, input("Enter the values with space seperated").split()))
head = create_linked_list(values)
print_list(head)

