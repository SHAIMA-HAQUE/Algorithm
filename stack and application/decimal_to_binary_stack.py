from stack_data_structure import Stack
from reverse_string_stack import reverse_string

def deci_to_bin(num,stack):
    if num == 0:
        return 0
    binary = ""
    while num > 0:
        stack.push(num%2)
        num = num//2
        
        binary = binary + str(stack.pop())
        

    return reverse_string(stack,binary)

stack = Stack()
print(deci_to_bin(242,stack))
print(deci_to_bin(0,stack))