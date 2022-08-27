class TreeNode:
    def __init__(self,data,left=None,right=None) -> None:
        self.data=data
        self.left=left
        self.right=right

    @staticmethod
    def preOrderTraversal(root):
        if not root:
            return
        print(root.data,end='->')
        TreeNode.preOrderTraversal(root.left)
        TreeNode.preOrderTraversal(root.right)

    @staticmethod
    def heightOfTree(root)->int:
        if root is None:
            return 0
        else:
            return max(TreeNode.heightOfTree(root.left),TreeNode.heightOfTree(root.right))+1

        
    @staticmethod
    def inOrderTraversal(root):
        if not root:
            return
        TreeNode.preOrderTraversal(root.left)
        print(root.data,end='->')
        TreeNode.preOrderTraversal(root.right)

    @staticmethod
    def postOrderTraversal(root):
        if not root:
            return
        TreeNode.preOrderTraversal(root.left)
        TreeNode.preOrderTraversal(root.right)
        print(root.data,end='->')

    
if __name__=="__main__":
    tree=TreeNode("Drinks")
    hotDrinks=TreeNode("Hot")
    coldDrinks=TreeNode("Cold")
    tree.left=hotDrinks
    tree.right=coldDrinks
    coffee=TreeNode("Coffee")
    tea=TreeNode("Tea")
    fanta=TreeNode("Fanta")
    cola=TreeNode("Cola")
    sprite=TreeNode("Sprite")
    hotDrinks.left=coffee
    hotDrinks.right=tea
    coldDrinks.left=fanta
    coldDrinks.right=cola

    print(TreeNode.heightOfTree(tree))

    print("PerOrder:")
    TreeNode.preOrderTraversal(tree)
    print("")
    print("InOrder:")
    TreeNode.inOrderTraversal(tree)
    print("")
    print("PostOrder:")
    TreeNode.postOrderTraversal(tree)