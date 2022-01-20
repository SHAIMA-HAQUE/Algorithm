class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        # return len(self.items) == 0
        return not self.items
    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
   
    s.push(7)
    s.push(8)
    print(s) 
    print(s.pop())    
    print(s)
    print(s.peek())
    print(s.size())
            