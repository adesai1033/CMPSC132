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
if __name__ == "__main__":
    import doctest
    doctest.run_docstring_examples(Complex, globals(), name='Rec3',verbose=True) # Uncomment this line if you want to run doctest by function. Replace get_words with the name of the function you want to run
    #doctest.testmod() # Uncomment this line if you want to run the docstring in all functions

