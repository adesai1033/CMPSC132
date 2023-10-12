# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

from cmath import inf
import random
import math

class Fibonacci:
    """
        >>> fib_seq = Fibonacci()
        >>> fib_seq
        <Fibonacci object>, value = 0
        >>> fib_seq.next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next().next()
        <Fibonacci object>, value = 3
        >>> fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
        >>> other_fib_seq = Fibonacci()
        >>> other_fib_seq
        <Fibonacci object>, value = 0
        >>> other_fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
    """
    #Constructor method
    def __init__(self):
        self.start = 0

    #Creates value outside of next
    #Creates fib obj everytime method called
    #In the first iteration fib value is one.. default case
    #Then adds previous numbers and obj points to this
    #self.start automatically updates because of __repr__
    #value attribute of obj create must be manually updated to self.start for next call of next
    #Returns obj
    value = 0
    def next(self):
        fib = Fibonacci() #Creates Fib obj
        if(self.start == 0):
            fib.start = 1
        else:
            fib.start = self.start + self.value
            fib.value = self.start
        return fib


    def __repr__(self):
        return f"<Fibonacci object>, value = {self.start}"


class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''
    #Initializes dictionary and balance
    #Dictionary key is item id and values are price and quantity respectively
    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.info = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]} 
        self.balance = 0
        pass


    #Processes purchase of items
    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        #If the item entered has an invalid id
        if(item not in self.info):
            return 'Invalid item'
        #If the machine is completely empty
        elif(self.isStocked == False):
            return 'Machine out of stock'
        #If item entered is out of stock
        elif(self.info[item][1] == 0):
            return 'Item out of stock'
        #If item is in stock but quantity desired exceeds amount in stock
        elif(self.info[item][1] - qty < 0):
            return f'Current {item} stock: {self.info[item][1]}, try again' 
        #If there are insufficient funds
        elif(self.balance < self.info[item][0]*qty):
            return f'Please deposit ${self.info[item][0]*qty - self.balance}'
        #If total cost results in no remainder
        elif(self.balance - self.info[item][0]*qty == 0):
            self.info[item][1] -= qty
            return 'Item dispensed'
        #If there is a remainder and change is due
        elif(self.balance - self.info[item][0]*qty > 0):
            self.info[item][1] -= qty
            change = self.balance -  self.info[item][0]*qty 
            self.balance = 0
            return f'Item dispensed, take your ${change} back'

        pass

        

    #Adds money to balance
    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        if(self.isStocked == False):
            return f'Machine out of stock. Take your ${amount} back'
        self.balance = amount
        return f'Balance: ${self.balance}'
        pass

    #Restocks certain items with certain amount
    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        if(item not in self.info):
            return 'Invalid item'
        else:
            self.info[item][1] += stock
        return f'Current item stock: {self.info[item][1]}'
        pass


    #--- YOUR CODE STARTS HERE
    @property
    #Checks if any items are non-zero
    def isStocked(self):
        stocked = False
        for key in self.info:
            if(self.info[key][1]!=0):
                stocked = True
        return stocked
        
        pass
        

    #--- YOUR CODE STARTS HERE
    @property
    #Returns updated dictionary
    def getStock(self):
        return self.info
        pass

    #Updates balance due to cancelled transaction
    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self.balance>0:
            change = self.balance
            self.balance = 0
            return f'Take your ${change} back'
        pass
       


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    #Constructor
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.point1 = point1
        self.point2 = point2
        pass

    #--- YOUR CODE STARTS HERE
    #Calculates distance using x and y components of each point
    @property
    def getDistance(self):
        x = (float)(self.point2.x) - (float)(self.point1.x) #Difference between x
        y = (float)(self.point2.y) - (float)(self.point1.y) #Difference between y
        return round(math.sqrt(x*x + y*y),3) #Distance formula
        pass
       
    
    #--- YOUR CODE STARTS HERE
    #Calculates slope using x & y components of each point
    @property
    def getSlope(self):
        x = (float)(self.point2.x) - (float)(self.point1.x) #Differences in x
        y = (float)(self.point2.y) - (float)(self.point1.y) #Differencds in y
        if((float)(self.point1.x) - float(self.point2.x) == 0): 
            return inf
        m = y/x
        return round(m,3)
        pass


    #--- YOUR CODE CONTINUES HERE
    #Formats slope into a line equation in form of y = mx + b
    #Checks if slope is valid and calculates intercept if so
    #If invalid returns Undefined
    def __str__ (self):
        m = self.getSlope 
        
        if(m!= inf and m!=0): #m must be valid
            b = round((float)(self.point1.y)-(float)((m*self.point1.x)),3) #y = mx + b -> b = y - mx
            return f'y = {m}x + {b}'
        elif m == 0.0:
            b = round((float)(self.point1.y)-(float)((m*self.point1.x)),3)
            return f'y = {b}'
        return 'Undefined'

    __repr__ = __str__

    #Multiplication of line and integer
    #Multiplies each component
    def __mul__(self,mul):
        x1= self.point1.x * mul 
        x2 = self.point2.x * mul
        y1 = self.point1.y * mul
        y2 = self.point2.y * mul
        return Line(Point2D(x1,y1),Point2D(x2,y2))
    #Backup method for multiplication of integer and line
    def __rmul__(self,mul):
        x1 = self.point1.x * mul 
        x2 = self.point2.x * mul
        y1 = self.point1.y * mul
        y2 = self.point2.y * mul
        return Line(Point2D(x1,y1),Point2D(x2,y2))

    #First checks if parameters are instances of Line
    #Then checks if both have same x and y components
    def __eq__(self,other):
        if(isinstance(self,Line) and isinstance(other,Line)):
            if(self.point1.x == other.point1.x and self.point2.y == other.point2.y):
                return True
        return False






if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(VendingMachine, globals(), name='Lab2',verbose=True) # replace Fibonacci for the class name you want to test
