class Node:
  def __init__(self , val):
      self.value = val
      self.left = None
      self.right = None

def maxDepth(root):
  # Null node has 0 depth.
  if root == None:
    return 0

  # Get the depth of the left and right subtree
  # using recursion.
  leftDepth = maxDepth(root.left)
  rightDepth = maxDepth(root.right)

  # Choose the larger one and add the root to it.
  if leftDepth > rightDepth:
    return leftDepth + 1
  else:
    return rightDepth + 1


# Function to find LCA of n1 and n2. The function assumes that both n1 and n2 are present in BST
def lca(root, n1, n2):
    if root is None:
        return None
    # If both n1 and n2 are smaller than root, then LCA lies in left
    if (root.value > n1 and root.value > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA lies in right
    if (root.value < n1 and root.value < n2):
        return lca(root.right, n1, n2)
    return root.value

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.left.right = Node(7)
print("The max depth is:", maxDepth(root))
print("Lower common ancestor :", lca(root, 4, 2))