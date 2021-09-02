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

    def len_iterative(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count
    
    def len_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def swap_node(self,key_1,key_2):

        if key_1 == key_2:
            return
        prev_node1 = None
        curr_node1 = self.head
        while curr_node1 and curr_node1.data != key_1:
            prev_node1 = curr_node1
            curr_node1 = curr_node1.next
        prev_node2 = None
        curr_node2 = self.head
        while curr_node2 and curr_node2.data != key_2:
            prev_node2 = curr_node2
            curr_node2 = curr_node2.next
        
        if not curr_node1 and not curr_node2:
            return
        if prev_node1 :
            prev_node1.next = curr_node2
        else:
            self.head = curr_node2
        
        if prev_node2:
            prev_node2.next = curr_node1
        else:
            self.head = curr_node1
        
        curr_node1.next, curr_node2.next = curr_node2.next, curr_node1.next
    
    def reverse_iterative(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next
        self.head = prev_node



# 

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.reverse_iterative()

llist.print_list()