from collections import deque

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

    @staticmethod
    def getKthNodesFromRoot(root,k): # print all nodes which are at a distance of k from root node
        if not root:
            return
        if k==0:
            print(root.data)
        # if k==2:                   # Added in first attempt but not required
        #     if root.left:
        #         print(root.left.data)
        #     if root.right:
        #         print(root.right.data)
        else:
            TreeNode.getKthNodesFromRoot(root.left,k-1)
            TreeNode.getKthNodesFromRoot(root.right,k-1)

    @staticmethod
    def levelOrderTraversal(root):
        if not root:
            return
        queue=deque()
        queue.append(root)
        while queue.__len__()>0:
           rootNode=queue.popleft() 
           print(rootNode.data)
           if rootNode.left:
            queue.append(rootNode.left)
            if rootNode.right:
                queue.append(rootNode.right)

            

    
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
    tea.left=TreeNode("Herbal")
    tea.right=TreeNode("Masala")
    coffee.left=TreeNode("Latte")
    coffee.right=TreeNode("Black")

    # print(TreeNode.heightOfTree(tree))

    # print("PerOrder:")
    # TreeNode.preOrderTraversal(tree)
    # print("")
    # print("InOrder:")
    # TreeNode.inOrderTraversal(tree)
    # print("")
    # print("PostOrder:")
    # TreeNode.postOrderTraversal(tree)
    # TreeNode.getKthNodesFromRoot(tree,2)
    TreeNode.levelOrderTraversal(tree)