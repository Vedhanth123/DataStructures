# program to convert infix to postfix

# algorithm:
# 1) Scan the infix expression from left to right
# 2) If the scanned character is an operand, output it
# 3) Else:
#       If the precedence and associativity of the scanned operand are greater than the operand present in the stack (or if the stack is empty then push the operand to the stack)
#       For operand '^' is right associative and other operators like '+','-','*' and '/' are left-associative. Check especially for a condition when both, operator at the top of the stack and the scanned operator are '^'. In this condtion, the precedence of the scanned operator is higer due to its right assocaitivity. So it will be pushed into the operator stack. In all the other cases when the top of the operator stack is the same as the scanned operator, then pop the operator from the satck because of left associativity due to which the scanned operator has less precedence.
#       Else, pop all the operators from the stack which are greater than or equal to in prededence than that of the scanned operator. After doing that PUsh the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.)
#   If the scanned character is an '(', push it to the stack
#   If the scanned character is an ')', pop the stack and output it until and '(' is encountered, and discard both the parenthesis.
#   Repeat steps 2-6 until the infix expression is scanned.
#   Print the output
# Pop and output form the stack until it is not empty.

# infix = input("Enter your infix expression")
infix = "a+b*c"

postfix = ""
stack = []

def infix_to_postfix(infix, postfix):

    # 2) If the scanned character is an operand, output it
    for x in infix:
        if(x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
            postfix += x
        if(x in '^')

