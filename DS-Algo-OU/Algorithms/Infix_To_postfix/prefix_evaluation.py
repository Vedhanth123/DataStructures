from Stack import Stack

# create a stack
Stk = Stack()

# take input of a string
def prefix_evaluation(string):

    traverser = -1

    # creating an operator string
    operators = "+-*/%"
    # traverse the string from last index to right till any operator arrives
    # while(string[traverser] not in operators or (traverser == -len(string))):
    while(True):

        if(string[traverser] not in operators or (traverser == -len(string))):
        # push operand to stack
            Stk.push(traverser)

            # decrement the traverser to point to the next element in string
            traverser -= 1
        else:
            oper1 = int(Stk.pop())
            oper2 = int(Stk.pop())

            if(string[traverser] == '+'):
                Stk.push(oper1 + oper2)
                traverser -= 1
            elif(string[traverser] == '-'):
                Stk.push(oper1 - oper2)
                traverser -= 1
            elif(string[traverser] == '*'):
                Stk.push(oper1 * oper2)
                traverser -= 1
            elif(string[traverser] == '/'):
                Stk.push(oper1 // oper2)
                traverser -= 1
            elif(string[traverser] == '%'):
                Stk.push(oper1 % oper2)
                traverser -= 1
            else:
                pass
            

prefix_evaluation('+*425')


        

    