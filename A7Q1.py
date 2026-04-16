class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def display(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None") 

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node  
    
    def delete(self, key):
        current = self.head
        if current is None:
            print("The list is empty. Nothing to delete.")
            return
        
        if current.data == key:
            self.head = current.next
            current = None
            print(f"Node with value {key} deleted.")
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            print(f"Node with value {key} not found.")
            return
        
        prev.next = current.next
        current = None
        print(f"Node with value {key} deleted.")
    
    def delete_at_beginning(self):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        self.head = self.head.next  
        print("Node at the beginning deleted.")
    
    def delete_at_end(self):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        current = self.head
        if current.next is None:
            self.head = None
            print("Last node deleted.")
            return
        while current.next and current.next.next:
            current = current.next
        current.next = None 
        print("Last node deleted.")

if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_beginning(5)
    
    print("Linked List:")
    linked_list.display()  
    
    linked_list.delete(20)  
    print("Linked List after deleting node with value 20:")
    linked_list.display()  
    
    linked_list.delete_at_beginning() 
    print("Linked List after deleting the first node:")
    linked_list.display() 
    
    linked_list.delete_at_end()  
    print("Linked List after deleting the last node:")
    linked_list.display()  

    linked_list.insert_at_end(40)  
    print("Linked List after inserting the last node:")
    linked_list.display()  
