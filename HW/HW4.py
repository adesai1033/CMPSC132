# HW4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# You might add additional methods to encapsulate and simplify the operations, but they must be
# thoroughly documented


from imp import is_frozen
from re import L


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.insert('mom')  
        >>> x.insert('omm') 
        >>> x.insert('mmo') 
        >>> x.root          
        Node({'mmo': ['mom', 'omm', 'mmo']})
        >>> x.insert('sat')
        >>> x.insert('kind')
        >>> x.insert('ats') 
        >>> x.root.left
        Node({'ast': ['sat', 'ats']})
        >>> x.root.right is None
        True
        >>> x.root.left.right
        Node({'dikn': ['kind']})
    '''

    def __init__(self):
        self.root = None


    # Modify the insert and _insert methods to allow the operations given in the PDF
    # Document all the modifications done
    def insert(self, value):
        valueSorted = ''.join(sorted(value))
        
        if self.root is None:
            self.root = Node({valueSorted: [value]}) #Creates node with value as dictionary instead of integer

        elif self.root is not None and valueSorted in self.root.value:
            self.root.value[valueSorted].append(value) #If the root is not empty but the key of the dictionary in the root is the same as valueSorted we append the original value to the current dictionary

        else:
            self._insert(self.root, value) #Calls helper method when the root is not empty and its key is not the same as valueSorted


    def _insert(self, node, value):
        
        valueSorted = ''.join(sorted(value))
        if valueSorted in node.value: #This is a new if condition 
            node.value[valueSorted].append(value) #Because node values are dictionaries we must check the node itself before checking left and right
            
        elif(valueSorted<list(node.value.keys())[0]): #if the sorted word is 'less' than the key in the dictionary of the current node
            
            if(node.left == None): #If node is empty
                node.left = Node({valueSorted: [value]}) #Create new dictionary as value of node
                
            elif node.left is not None and valueSorted in node.value: #If the node already has a dictionary and the key is the same as valueSorted
                node.value[valueSorted].append(value) #We append to the current dictionary in the node

            else:
                self._insert(node.left, value) #Else we go further left
                
        else:
            
            if(node.right==None): #If the node to right is empty
                node.right = Node({valueSorted: [value]}) #Create new dictionary as value of node
                
            elif node.right is not None and valueSorted in node.value: #If the node is not empty but its dictionary's key is the same as valueSorted
                node.value[valueSorted].append(value) #Append the original value to the dictionary stored in the node
                
            else:
                self._insert(node.right, value) #Otherwise we go further right

    def isEmpty(self):
        return self.root == None

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

    def printPostOrder(self):
        if self.isEmpty():
            return None
        else:
            self._postorderHelper(self.root)

    def _postorderHelper(self, node):
        if node is not None:
            self._postorderHelper(node.right) 
            print(node.value, end=' : ') 
            self._postorderHelper(node.left)
        
    



class Anagrams:
    '''
        # Verify class has _bst attribute  
        >>> x = Anagrams(5)
        >>> '_bst' in x.__dict__    
        True
        >>> isinstance(x.__dict__.get('_bst'), BinarySearchTree)
        True
        >>> x = Anagrams(5)
        >>> x.create('words_small.txt')
        >>> x.getAnagrams('tap')
        'No match'
        >>> x.getAnagrams('arm')
        'No match'
        >>> x.getAnagrams('rat')
        ['art', 'tar', 'rat']
        >>> x._bst.printInorder
        {'a': ['a']} : {'adns': ['ands', 'sand']} : {'ahms': ['sham', 'hams']} : {'amt': ['tam', 'mat']} : {'arst': ['arts', 'rats', 'star']} : {'arsty': ['artsy']} : {'art': ['art', 'tar', 'rat']} : 
    '''
    
    def __init__(self, word_size):
        # -YOUR CODE STARTS HERE
        self.word_size = word_size #Maximum Word Size
        self._bst = BinarySearchTree() #Creates BST obj
        pass




    def create(self, file_name):
        # -YOUR CODE STARTS HERE
        # Code for reading the contents of file_name is given in the PDF
        with open(file_name) as f: #opens file
            contents = f.read().split('\n') #Textfile is words each in their own line so we split by \n
            
            for i in contents:
                if len(i)<=self.word_size and i != '': #check if the word meets the constraint of the max word_size we initialized and that it is not empty
                    self._bst.insert(i) #Calls BST insert method to create tree of nodes with values of dictonaries
        f.close() #closes file
       
        
            
        pass


    def getAnagrams(self, word):
        # -YOUR CODE STARTS HERE
        wordSorted = ''.join(sorted(word)) #sorted word
        current = self._bst.root #Start at root of tree
        
        while current:

            if list(current.value.keys())[0] < wordSorted: #Uses properites of BST
                current = current.right #If the current value is smaller than the desired value we want a larger value and will go right
                
            elif list(current.value.keys())[0] > wordSorted:
                current = current.left #If the current value is greater than the desired value we want a smaller value and will go left
   
            else:
                return current.value[list(current.value.keys())[0]] #We have found the node which has the dictionary of all words with the same letters and we return this
            
        return 'No match' #If nothing was previously returned we did not find an anagram
        
        pass


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    #doctest.run_docstring_examples(Anagrams, globals(), name='HW4',verbose=True) 
