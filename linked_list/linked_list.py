class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append_after_node(self,prev_node,data):
        new_node = Node(data)
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node
    #deleting node by value
    def delete_node(self,key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        while curr_node and curr_node.data!=key:
            prev_node = curr_node
            curr_node = curr_node.next

            if curr_node == None:
                return
            prev_node.next = curr_node
            curr_node = None
    
    #deleting node by position
    def delete_not_at_position(self,pos):
        if self.head:
            curr_node = self.head
            if pos == 0:
                self.head = curr_node.next
                curr_node = None
                return
        prev_node = None
        count = 0
        while curr_node and count!=pos:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
            
            if curr_node == None:
                return

            prev_node.next = curr_node.next
            curr_node = None

            


linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")

linked_list.prepend("C")
linked_list.append_after_node(linked_list.head.next,"Yoda")
linked_list.delete_node("C")
linked_list.delete_not_at_position(1)
linked_list.print_list()