# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree: #47, 5, 3, 70, 23, 53, 15, 66, 81, 64, 85, 31, 83, 33, 9, 7
    
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)    
    @property
    def printPostorder(self):
 
        if self.root:
 
        # First recur on left child
            self.printPostorder(self.root.left)
 
        # the recur on right child
            self.printPostorder(self.root.right)
 
        # now print the data of node
            print(self.root.val),     


    def mirror(self):
        # Creates a new BST that is a mirror of self: 
        #    Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree
        




    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.root == None
        pass



    def _mirrorHelper(self, node):
        # YOUR CODE STARTS HERE
        #Recursively iterate through left subtree then recursively iterate through right subtree
        #Base Case
        #Movement
        #Recursive Call
        if node == None: #When you have reached end of sub tree
            return
        else:
            newNode = Node(node.value)
            newNode.right = self._mirrorHelper(node.left) #First evaluates left subtree
            newNode.left = self._mirrorHelper(node.right) #Once left side has been finished right side begins 
            
            return newNode #Returns mirrored tree
        
        

        
        pass



    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        currentMin = self.root
        while currentMin.left:  #Uses property of BinarySearchTree that smallest value will be on the left
            currentMin = currentMin.left
        return currentMin
        pass



    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE
        currentMax = self.root
        while currentMax.right: #Uses property of BinarySearch Tree that largest value will be on the right
            currentMax = currentMax.right
        return currentMax
        pass



    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        #Greater values on right lesser values on left
        current = self.root
        while current:
            if current.value < value: #Uses properites of BST
                current = current.right #If the current value is smaller than the desired value we want a larger value and will go right
            elif current.value > value:
                current = current.left #If the current value is greater than the desired value we want a smaller value and will go left
            else:
                return True
        return False
        pass



    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        if node == None or node.left == None and node.right == None: #When we have reached end of loop
            return 0 
            
        if self.getHeight(node.left) > self.getHeight(node.right): #Checks which side is larger
            return self.getHeight(node.left) + 1
        else:
            return self.getHeight(node.right) + 1
 
        
        pass


if __name__=='__main__':
    x = BinarySearchTree()
    #47, 5, 3, 70, 23, 53, 15, 66, 81, 64, 85, 31, 83, 33, 9, 7
    x.insert(47)
    x.insert(5)
    x.insert(3)
    x.insert(70)
    x.insert(23)
    x.insert(53)
    x.insert(15)
    x.insert(66)
    x.insert(81)
    x.insert(64)
    x.insert(85)
    x.insert(31)
    x.insert(83)
    x.insert(33)
    x.insert(9)
    x.insert(7)
    x.printInorder
    x.printPostorder
    
