from stack_data_structure import Stack

def reverse_string(stack , og_string):
    for i in range(len(og_string)):
        stack.push(og_string[i])
    rev_string = ""
    while not stack.is_empty():
        rev_string = rev_string + stack.pop()
    
    return rev_string

stack = Stack()
input_str = "!dlroW olleH"
print(reverse_string(stack, input_str))
    
# import stack 

# string = "!dlroW olleH"
# reversed_string = ""
# s = stack.Stack()

# for char in string:
#     s.push(char)
    

# while not s.is_empty():
#     reversed_string += s.pop()


# print(reversed_string)