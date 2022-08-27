class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children

    def addChild(self,treeNode):
        self.children.append(treeNode)

    def addChildren(self,treeNodes):
        self.children.extend(treeNodes)

    def __str__(self,level=0) -> str:
        rep=" "*level + str(self.data) + "\n"
        for child in self.children:
            rep+= child.__str__(level+1)
        return rep

if __name__=="__main__":
    tree=TreeNode("Drinks",[])
    hotDrinks=TreeNode("Hot",[])
    coldDrinks=TreeNode("Cold",[])
    # tree.addChild(hotDrinks)
    # tree.addChild(coldDrinks)
    tree.addChildren([hotDrinks,coldDrinks])
    coffee=TreeNode("Coffee",[])
    tea=TreeNode("Tea",[])
    fanta=TreeNode("Fanta",[])
    cola=TreeNode("Cola",[])
    sprite=TreeNode("Sprite",[])
    # hotDrinks.addChild(coffee)
    # hotDrinks.addChild(tea)
    hotDrinks.addChildren([coffee,tea])
    # coldDrinks.addChild(fanta)
    # coldDrinks.addChild(cola)
    coldDrinks.addChildren([fanta,cola,sprite])


    print(tree)