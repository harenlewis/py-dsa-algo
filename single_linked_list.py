class Node(self):
    def __init__(self, data=None, next=None):
        self.data = None
        self.next = None


class LinkedList(self):
    def __init__(self):
        self.head = None

    def print(self):
        if not self.head:
            print("Linked List is empty!")

        current_node = self.head
        while current_node.next:
            print(current_node.data)
            current_node = current_node.next

    def insert_values(self, data):
        current_node = self.head

        for val in data:
            new_node = Node(val)
            current_node.next = new_node
            current_node = new_node

    def insert_at_begining(self, data):
        next_node = None
        if self.head:
            next_node = self.head

        new_start_node = Node(data, next_node)
        self.head = new_start_node

    def insert_at_end(self, data):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)

    def insert_at_index(self, index, data):
        if index == 0:
            self.head = Node(data, self.head)
        
        new_node = Node(data)

        current_index = 0
        current_node = self.head

        while current_node.next:
            if current_index == i-1:
                current_node.next = current_node.next
    
            current_node = current_node.next
            i+=1

    def remove_at_index(self, index, data):
        if index==0:
            self.head = self.head.next
            return

        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index - 1:
                current_node.next = current_node.next.next
                break

            current_node = current_node.next
            current_index+=1 

    def get_lenght(self):
        ll_len = 0

        current_node = self.head

        while current_node.next:
            ll_len +=1
            current_node = current_node.next

        print("Linked List lenght: ", ll_len)


"""
Time Complexitiy

Inset/Delete element at start: O(1)

Inset/Delete element at end: O(n)

Inset element in middle: O(n)
"""
