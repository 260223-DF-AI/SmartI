
"""
    A class representing arithmetic operations.

     Let's say we're making a calculator app!
    
"""

# Good to go

def add_numbers( a, b):
        """
        * Instead of returning 0, this method should return the sum of two integers (ints).
        * Ints represent whole numbers in Python.
        *
        * @param a first number to be added.
        * @param b second number to be added.
        * @return the sum of a and b

        """
        return a + b

def subtract_numbers( a, b):
        """
        * Instead of returning 0, this method should return the difference between two integers (ints).
        
        Args:
        a (int): The first number.
        b (int): The second number.

        * @return the difference of a and b

        """
        return a - b

def multiply_numbers( a, b):
        """
        Instead of returning 0,This method should return the product of two numbers.

        :param a: first number.
        :param b: second number.
        :return: the product of a and b.
        """
        return a * b
    

def divide_numbers( a, b):
        """
        Instead of returning 0, This method should return the result of dividing the first number by the second number.

        :param a: first number (dividend).
        :param b: second number (divisor).
        :return: the result of dividing a by b.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b    

def modulus_numbers( a, b):
    """
    Instead of returning 0,This method should return the remainder of dividing the first number by the second number.

        :param a: first number (dividend).
        :param b: second number (divisor).
        :return: the remainder of dividing a by b.
    """
    if b == 0:
        raise ValueError("Cannot take modulus by zero")
    return a % b


    


       