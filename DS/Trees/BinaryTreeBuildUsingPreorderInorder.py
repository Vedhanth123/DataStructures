
class BinaryTree:

    # head will be none if the head is not declared
    root = None

    # declaring head
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

        # checking if the root is empty or not
        if (BinaryTree.root == None):
            root = self

    def display(self):
        print(self.data)

    def addright(self):
        pass

    def preorder(self, node):

        if (node != None):

            print(node.data, end=",")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):

        if (node != None):

            self.inorder(node.left)
            print(node.data, end=",")
            self.inorder(node.right)

    def postorder(self, node):

        if (node != None):

            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=",")

    @staticmethod
    def preorder_build(preorder, inorder, start, end, idx):

        # algorithm:
        # 1) Pick element from preorder and create a node
        # 2) Increment preorder idx
        # 3) search for picked element's pos in inorder
        # 4) Call to build left subtree from inorder's 0 to pos-1
        # 5) Call to build right subtree from inorder pos+1 to n
        # 6) Return the node

        # 1) Pick element from preorder and create a node
        node = BinaryTree(preorder[idx])

        # 2) Increment preorder idx
        idx += 1
        
        # 3) Search for the picked element's pos in inorder
        pos = 0
        for x in range(len(inorder)):

            if(inorder[x] == preorder[idx-1]):
                pos = x
                break
        
        # 4) building left subtree
        node.left = BinaryTree.preorder_build(preorder, inorder, start, pos-1, idx)

        # 5) building right subtree
        node.right = BinaryTree.preorder_build(preorder, inorder, pos+1, end, idx)

        # 6) Return the node
        return node
        


node = BinaryTree.preorder_build("12435", "42153", 0, 4, 0)


