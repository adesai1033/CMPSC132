#Lab #0
# More information on pass statement: 
#    https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement
def sumSquares(numList):
    """
        >>> sumSquares([1,5,-3,5.5,359,8,14,-25,1000])
        1129171.25
        >>> sumSquares([14,5,-3,5,9.0,8,14,7,-846])
        586.0
        >>> sumSquares([-8,-4,1,2,3,4,5,6])
        132
        
    """
    # --- YOU CODE STARTS HERE
    total = 0
    for x in numList:
        if(x>5 and x<500 or x%4 == 0):
            total += x*x
    return total
if __name__ == "__main__":
    import doctest
    doctest.testmod()
