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


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Original List")
llist.print_list()


llist.swap_node("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

llist.swap_node("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()

llist.swap_node("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()

llist.swap_node("C", "C")
print("Swapping nodes C and C where both keys are same")
llist.print_list()
            


linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")

linked_list.prepend("C")
linked_list.append_after_node(linked_list.head.next,"Yoda")
linked_list.delete_node("C")
linked_list.delete_not_at_position(1)
linked_list.print_list()
print(linked_list.len_iterative())
print(linked_list.len_recursive(linked_list.head))