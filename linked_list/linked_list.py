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
    def reverse_recursive(self):
        def _reverse_iterative(curr_node, prev_node):

            if not curr_node:
                return prev_node
        
            next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next

            return _reverse_recursive(curr_node,prev_node)
        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        self.head = new_head
        return self.head

    def remove_duplicates(self):
        curr_node = self.head
        prev_node = None
        dup_values = dict()

        while curr_node:
            if curr_node.data in dup_values:
                prev_node.next = curr_node.next
                curr_node.next = None
            else:
                dup_values[curr_node.data] = 1
                prev_node = curr_node
            curr_node = prev_node.next

    def nth_to_last(self,n):
        total_len = self.len_iterative()

        curr_node = self.head
        while curr_node:
            if total_len == n:
                print(curr_node.data)
                return curr_node.data
            total_len-=1
            curr_node = curr_node.next
        if curr_node is None:
            return


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

# llist.reverse_iterative()

# llist.print_list()

# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge(llist_2)
# llist_1.print_list()

# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)

# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()

print(llist.nth_to_last(4))
