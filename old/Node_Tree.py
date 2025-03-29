class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        self.size = self.size + 1

    # Fixed all the issues with the code. /
    # Added the correct methods to the BinarySearchTree Class. /
    # The missing methods were __setitem__, get, _get, and __getitem__.
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)

        # An additional condition is added to handle scenarios where a key is larger than the current node's key.
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

        # This condition statement handles keys that are equal to each other.
        else:
            # Must use TreeNode's replaceNodeData function to properly overwrite keys.
            currentNode.replaceNodeData(
                key, val, currentNode.leftChild, currentNode.rightChild
            )

    # This method is in the book, it is the driver for the "put" function. /
    # Must be present for the main function to assign keys/values to nodes.
    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    # This method is the driver for the "get" function. /
    # Must be present for the main function to print values instead of objects.
    def __getitem__(self, key):
        return self.get(key)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


# Added a main module to be used as the driver for the code.
def main():

    inTree = BinarySearchTree()

    # Nodes in the tree are being assigned new keys and values. /
    # The bracketed numbers are becoming keys and the strings are becoming values.
    inTree[1] = "Mercury"
    print(inTree[1])

    inTree[2] = "Venus"
    print(inTree[2])

    inTree[3] = "Earth"
    print(inTree[3])

    inTree[4] = "Mars"
    print(inTree[4])

    # This example specifically tests if the code can handle duplicate keys.
    inTree[1] = "Jupiter"
    print(inTree[1])


main()
