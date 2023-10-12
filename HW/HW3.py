# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> len(x)
        0
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None #If self.top is none the Stack is empty
     
        passm

    def __len__(self): 
        # YOUR CODE STARTS HERE
   
        count = 0 
        current = self.top
        while current:  #Iterates until the next of the node points to none
            count += 1
            current = current.next
        return count
        pass

    def push(self,value):
        # YOUR CODE STARTS HERE
        nTop = Node(value) #Creates node object
        nTop.next = self.top #New node should be the top so node's next is assigned to current top
        self.top = nTop #Top is redfined
        pass

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if not self.isEmpty(): #Prevens errors
            temp = self.top #Stores node we are popping so we can return the value
            self.top = self.top.next #Top is updated
            temp.next = None #Previous top delinked
            return temp.value
        pass

    def peek(self):
        # YOUR CODE STARTS HERE
        return self.top.value #Returns value of top
        pass


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt) #Tries converted txt to float
        except:
            return False #If there is an error returns False
        return True #If there is no error, returns True
        pass




    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
            >>> x._getPostfix('7 ^ 2 ^ 3')
            '7.0 2.0 3.0 ^ ^'
            

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 $ 5')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix ('( ( 2  )')
            >>> x._getPostfix ('2 3 4')
            >>> x._getPostfix (') 2 (')
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + 2 ( 1 + 4 ) (')
            >>> x._getPostfix('( 2 * 3 ) + ( 2 + 3 )')
            '2.0 3.0 * 2.0 3.0 + +'
            >>> x._getPostfix('a*(b+c))/ d')
            '2.0 3.0 * 2.0 3.0 + +'

            
        
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        postfixStr = ""
        priority = {'(':0, '+':1, '-':1, '*':2, '/':2, '^':3}
        validOp = '^*/+-'
        parenthesis = '()'
        expr = txt.split()
        
        
        if len(expr)%2 == 0: #Parenthesis must always be an even amount, and operators/operand must be even/odd or vise-versa #even + odd + even = odd
            return None
        
        if expr.count('(') != expr.count(')'): #parenthesis must be closed so there should be equal amount
            return None
        '''
        for p in expr:
            if p in parenthesis:
                parenLst.append(p)
        
        half1 = parenLst[:len(parenLst)//2]
        half2 = parenLst[len(parenLst)//2:]
        
        if len(half1)%2 != 0: 
            if half1.count(half1[0]) != len(half1) or half2.count(half2[0]) != len(half2):
                return None
        '''

        if self._isNumber(expr[0]) == False and expr[0] != '(': #First item of list must either be a number or a (
            return None

        if self._isNumber(expr[-1]) == False and expr[-1]!= ')': #Last item of list msut either be a number or a )
            return None
        
        for i in range(1,len(expr)-1):
            if self._isNumber(expr[i]) and (self._isNumber(expr[i-1] or self._isNumber(expr[i+1]))): #If 2 numbers are next to eachother expression invalid
                return None
                
            elif self._isNumber(expr[i]) == False and expr[i] not in validOp and expr[i] not in parenthesis: #If the item is not a number, operator, or () it is invalid
                return None

            elif expr[i] in validOp and (expr[i-1] in validOp or expr[i+1] in validOp ): #Operators cannot be next to eachother
                return None

            elif expr[i] == '(' and expr[i+1] == ')': #Opening and closing parenthesis cannot be next to eachother
                return None

        
        #If expression is valid
        for ch in expr:
            if self._isNumber(ch):
                postfixStr += str(float(ch)) + ' ' #Add to final string if number
            else:
                if postfixStack.isEmpty():
                    postfixStack.push(ch) #Add operator to stack if Stack is empty

                elif ch == '(':
                    postfixStack.push(ch) #Push '(' to stack

                elif ch == ')': #Iterates until opening parenthesis is found
                    while postfixStack.peek() != '(' and postfixStack.isEmpty() == False:
                        postfixStr += postfixStack.pop() + ' ' #Pops to final strng
                    if postfixStack.isEmpty() == False: #Prevents runtime error
                        postfixStack.pop() 
            
                
                elif priority[postfixStack.peek()] < priority[ch]:
                    postfixStack.push(ch) #Higher priority can be pushed to stack

                elif postfixStack.peek() == ch and ch == '^':
                    postfixStack.push(ch) #Less than or equal precedence cannot be pushed to stack except for ^ because it is right associated

              
                else: #if priority is less than or equal
                    temp = postfixStack.peek()
                    
                    while postfixStack.isEmpty() == False and priority[temp] >= priority[ch]: #Pops until we can push ch to stack
                        postfixStr += postfixStack.pop() + ' '  #Adds to final string
                        if postfixStack.isEmpty() == False: 
                            temp = postfixStack.peek()
                    postfixStack.push(ch)

        while not postfixStack.isEmpty():
            if postfixStack.peek() != ')' and postfixStack.peek() != '(': 
                postfixStr += postfixStack.pop() + ' ' #Final postfix expression is everything in Stack except for parenthesis
            else:
                postfixStack.pop()             #pops so we can continue iterating through Stack

        return postfixStr.rstrip() #Removes leading & trailing spaces

        pass


    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        postfix = self._getPostfix(self.__expr)
        if postfix != None:
            postfix = postfix.split()
        else:
            return 
    
        for ch in postfix: #Iterates through postfix expression 
            if self._isNumber(ch):
                calcStack.push(ch)
            else: #formula shown in lecture
                num1 = float(calcStack.pop())  
                num2 = float(calcStack.pop())     
                if ch == '+':
                    calcStack.push(num2 + num1) #Pushes sum of 2 numbers
                elif ch == '-':
                    calcStack.push(num2 - num1) #Pushes difference of 2 numbers
                elif ch == '*': 
                    calcStack.push(num2 * num1) #Pushes multiplication of 2 numbers
                elif ch == '/':
                    calcStack.push(num2/num1) #Pushes division of 2 numbers
                elif ch == '^':
                    calcStack.push(num2**num1) #Pushes exponent of 2 numbers
        result = calcStack.pop() #At the end stack length should be 1
        if(len(calcStack) > 0):
            return None
        return result
            

        # YOUR CODE STARTS HERE
        pass

#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word): #A valid variable name is a non-empty string of alphanumeric characters, the first of which must be a letter
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
            >>> C._isVariable('A')
            True
        '''
        # YOUR CODE STARTS HERE
        if isinstance(word, str) == False or len(word) == 0 or word[0].isalpha() == False: #if input not a string or word is length 0 or first character is not letter
            return False

        for ch in word:
            if ch.isalpha() == False and ch.isalnum() == False:  #if not a letter or number
                return False
        return True
        pass
       

    def _replaceVariables(self, expr): #Replaces all variables in the input expression with the current value of those variables saved in self.states
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        lst = expr.split()
        isFound = False
        for i in range(len(lst)):
            if lst[i] in self.states:
                isFound = True
                lst[i] = str(self.states[lst[i]]) #Replaces variable with value from self.states
        if isFound:
            return ' '.join(lst) #String format
        
        elif len(expr) > 0 and (any(c.isalpha() for c in expr) == False): #if anything inside the expressoin is a letter
            return expr
        
        else:
            return None
        pass

    
    def calculateExpressions(self): #expressions are stored in self.states
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        #Split up expressions line by line (;)
        #Split up expression into left & right (=)
        result = {}

        expressions = self.expressions.split(';') #splits lines
        for i in range(len(expressions)):
            if 'return' in expressions[i]: 
                calcObj.setExpr(self._replaceVariables(" ".join(expressions[i].split()[1:]))) #return is first element in list so dont incldue
                result['_return_'] = float(calcObj.calculate) #key _return_ value is calculation
                break #exit loop
            else:
                exp = expressions[i].split('=')  # idx 0 is variable idx 1 is expression
                exp[0] = exp[0].strip() #Removds white spaces
                exp[1] = exp[1].strip()
                if self._isVariable(exp[0]) == False: #if the variable name is invalid
                    self.states = {} #reset states
                    return None #return None
                else:
                    calcObj.setExpr(self._replaceVariables(exp[1])) #sets expression uses replace variables
                    self.states[exp[0].rstrip()] = float(calcObj.calculate) #key is variable value is calculation
            temp = {} #Temporary dictionary
            for key in self.states:
                if 'return' not in key:
                    temp[key] = self.states[key] #each step of calculations
            result[expressions[i]] = temp #value is current state of dictionary

        return result
 
        pass

if __name__=='__main__':
    #import doctest
    #doctest.testmod(verbose=True)  # OR
   
    #doctest.run_docstring_examples(Calculator._getPostfix, globals(), name='HW3',verbose=True) 
    x = "((a+b)/e)+((c−d)*f)".replace(" ","")
    print(x)