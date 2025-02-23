class Node:
    # Node class represents a single node in the linked list
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node
    
class SinglyLinkedList:
    # SinglyLinkedList class to manage the linked list
    def __init__(self):
        self.head = None  # Initialize head as None

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if not self.head:  # If list is empty, new node becomes the head
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node  # Link last node to the new node

    def insert_at_front(self, data):
        # Insert a new node at the front (beginning) of the list
        new_node = Node(data)
        new_node.next = self.head  # Link new node to the current head
        self.head = new_node  # Update head to the new node
        self.display()

    def insert_at_npos(self, pos, data):
        # Insert a new node at a specific position
        new_node = Node(data)
        temp = self.head

        for i in range(1, pos):  # Traverse to the (pos-1) node
            prev = temp
            temp = temp.next

        prev.next = new_node  # Link previous node to the new node
        new_node.next = temp  # Link new node to the next node
        self.display()

    def display(self):
        # Display all nodes in the linked list
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")  # Print node data
            temp = temp.next
        print("NULL")  # Indicate end of the list

    def delete_at_npos(self, pos):
        # Delete a node at a specific position
        temp = self.head
        if not temp:
            print("List is empty")
            return
        for i in range(1, pos):  # Traverse to the (pos-1) node
            prev = temp
            temp = temp.next
        prev.next = temp.next  # Skip the node to be deleted
        self.display()

    def delete_first(self):
        # Delete the first node
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next  # Move head to the next node
        self.display()

    def delete_last(self):
        # Delete the last node
        if not self.head:
            print("List is empty")
            return
        if self.head.next is None:  # If only one node exists
            self.head = None
            self.display()
            return
        temp = self.head
        while temp.next.next:  # Traverse to second last node
            temp = temp.next
        temp.next = None  # Remove reference to last node
        self.display()

    def update(self, position, value):
        # Update the value of a node at a specific position
        temp = self.head
        for i in range(1, position):  # Traverse to the node
            temp = temp.next
        temp.data = value  # Update the node's value
        self.display()


sll = SinglyLinkedList()

while True:
    # Display menu for user operations
    print("\nChoose an operation:")
    print("1. Insert at End")
    print("2. Insert at Front")
    print("3. Insert at N Position")
    print("4. Delete First Node")
    print("5. Delete Last Node")
    print("6. Delete at N Position")
    print("7. Update a Node")
    print("8. Display List")
    print("9. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        data = int(input("Enter value to insert at end: "))
        sll.insert_at_end(data)
    elif choice == 2:
        data = int(input("Enter value to insert at front: "))
        sll.insert_at_front(data)
    elif choice == 3:
        pos = int(input("Enter position to insert: "))
        data = int(input("Enter value: "))
        sll.insert_at_npos(pos, data)
    elif choice == 4:
        sll.delete_first()
    elif choice == 5:
        sll.delete_last()
    elif choice == 6:
        pos = int(input("Enter position to delete: "))
        sll.delete_at_npos(pos)
    elif choice == 7:
        pos = int(input("Enter position to update: "))
        value = int(input("Enter new value: "))
        sll.update(pos, value)
    elif choice == 8:
        sll.display()
    elif choice == 9:
        break  # Exit the loop
    else:
        print("Invalid choice, please try again.")
