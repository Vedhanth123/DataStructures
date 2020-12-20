# Stack is a class name which is defined by me
class Stack:

    # these are functions in Stack class
    def __init__(self):
        self.array = []

    def push(self,number):
        self.array.append(number)

    def pop(self):
        self.array.pop()
    
    def seek(self):
        return self.array[len(self.array)-1]
        # print(self.array[len(self.array)-1])
    
    def isempty(self):
        return not len(self.array)
    
    def length(self):
        return len(self.array)

    def printer(self):
        return self.array


"""    
if name == "__main__":

    new_stack = Stack()

    new_stack.push(23)


    print(new_stack.isempty())

    print(new_stack.length())
    print(new_stack.array[new_stack.length()-2])
"""