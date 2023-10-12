class Complex:
    '''
        >>> a=Complex(5,-6)
        >>> b=Complex(2,14)
        >>> a*b
        94 + 58i
        >>> b*5
        10 + 70i
        >>> 5*b
        10 + 70i
        >>> isinstance(5*b, Complex)
        True
        >>> a.conjugate()
        5 + 6i
        >>> b.conjugate()
        2 - 14i
    '''
    def __init__(self,r,i):
        self._real = r
        self._imag = i
    def __str__(self):
        """Display complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"
        else:
           return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__
    def conjugate(self):
        return Complex(self._real,-self._imag)
    def __mul__(self,other):
        if(isinstance(other,Complex)):
            real = self._real * other._real - self._imag * other._imag
            imag = self._real*other._imag + other._real * self._imag
        else:
            real = other * self._real
            imag = other * self._imag
        return Complex(real,imag)
    def __rmul__(self,other):
        """Multiply a real and Complex number"""
        if(isinstance(self,Complex)):
            real = other * self._real
            imag = other * self._imag
        elif(isinstance(other,Complex)):
            real = self * other._real
            imag = self * other._imag
        return Complex(real,imag)
class Real(Complex):

    ''' Returns True if other is a Real object that has the same value or if other is
        a Complex object with _imag=0 and same value for _real, False otherwise
        >>> Real(4) == Real(4)
        True
        >>> Real(4) == Real(4.0)
        True
        >>> Real(5) == Complex(5, 0)
        True
        >>> Real(5) == Complex(5, 12)
        False
        >>> Real(5) == 5.5
        False
    '''
    def __init__(self, value):
        super().__init__(value, 0)

    def __mul__(self,other):
        if(isinstance(other,Real)):
            return Real(self._real*other._real)
        elif(isinstance(other,int)):
           return Real(other*self._real)
        elif(isinstance(other,float)):
           return Real(other*self._real)
        elif(isinstance(other,Complex)):
            real = self._real * other._real - self._imag * other._imag
            imag = self._real*other._imag + other._real * self._imag
            return Complex(real,imag)
    def __rmul__(self,other):
        if(isinstance(other,Real)):
            return Real(self._real*other._real)
        elif(isinstance(other,int)):
           return Real(other*self._real)
        elif(isinstance(other,float)):
           return Real(other*self._real)
        elif(isinstance(other,Complex)):
            real = self._real * other._real - self._imag * other._imag
            imag = self._real*other._imag + other._real * self._imag
            return Complex(real,imag)
    
    def __eq__(self, other):

        ''' Returns True if other is a Real object that has the same value or if other is
            a Complex object with _imag=0 and same value for _real, False otherwise

            >>> Real(4) == Real(4)
            True
            >>> Real(4) == Real(4.0)
            True
            >>> Real(5) == Complex(5, 0)
            True
            >>> Real(5) == Complex(5, 12)
            False
            >>> Real(5) == 5.5
            False
        '''
        # YOUR CODE STARTS HERE
        isEq = False
        if isinstance(self,Real) and isinstance(other,Real):
            if(self._real == other._real):
                isEq = True
        elif isinstance(self,Real) and isinstance(other,Complex):
            if(self._real == other._real and other._imag == 0):
                isEq = True
        return isEq
    def __int__(self):
        return int(self._real)
    def __float__(self):
        return float(self._real)
if __name__ == "__main__":
    import doctest
    doctest.run_docstring_examples(Real, globals(), name='Rec4',verbose=True) # Uncomment this line if you want to run doctest by function. Replace get_words with the name of the function you want to run
    #doctest.testmod() # Uncomment this line if you want to run the docstring in all functions

