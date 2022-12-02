# Tree program

class Tree:

    # creating a constructor and assigning value to the node here itself
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:

    # head will be none if the head is not declared
    root = None
    
    # declaring head
    def __init__(self, data) -> None:
        self.node = Tree(data)

        # checking if the root is empty or not
        if(BinaryTree.root == None):
            root = self.node
    
    def display(self):
        print(self.node.data)

    def preorder():
        pass
    
    def postorder():
        pass

    def inorder():
        pass


if __name__ == '__main__':

    # creating a tree
    obj = BinaryTree(5)

    obj.display()

