class BinaryTreeNode:

  def __init__(self, data):
    self.data = data
    self.leftchild = None
    self.rightchild = None


  def __str__(self, level=0):
    ret = "  " *level + str(self.data) + "\n"
    if self.leftchild:
       ret += self.leftchild.__str__(level+1)
    if self.rightchild:
       ret += self.rightchild.__str__(level+1)
    return ret


def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)

root = BinaryTreeNode("Peliculas")

Fantasia = BinaryTreeNode("Fantasia")
Comedia = BinaryTreeNode("Comedia")

Fantasia.leftchild = BinaryTreeNode("Epica")
Fantasia.rightchild = BinaryTreeNode("Infantil/Juvenil")

Fantasia.leftchild.leftchild =  BinaryTreeNode("El señor de los anillos")
Fantasia.leftchild.rightchild = BinaryTreeNode("mortal combat")

Fantasia.rightchild.leftchild = BinaryTreeNode("Harry Potter")
Fantasia.rightchild.rightchild = BinaryTreeNode("Cronicas Narnia")

Comedia.leftchild = BinaryTreeNode("Muertos del susto")
Comedia.rightchild = BinaryTreeNode("Donde esta el policia")

root.leftchild = Fantasia
root.rightchild = Comedia


print("Arbol con str")
print("\n")
print(root)

print("Arbol con printTree")
print("\n")
printTree(root)