# src/main/lab.py
# Good to go
def demonstrate_integer():
    """
    This function demonstrates the integer data type in Python.

    Create an integer variable named 'my_integer' and assign it any integer value.
    An integer is a whole number without any decimal points.
    """

    my_integer = 2  # Assign any integer value to 'my_integer'
    return my_integer


def demonstrate_float():
    """
    This function demonstrates the float data type in Python.
    
    Create a float variable named 'my_float' and assign it any floating-point value.
    A float is a number that has both an integer and fractional part, separated by a decimal point.
    """

    my_float = 3.1415926  # Assign any floating-point value to 'my_float'
    return my_float


def demonstrate_boolean():
    """
    This function demonstrates the boolean data type in Python.
    
    Create a boolean variable named 'my_boolean' and assign it either True or False.
    A boolean represents one of two values: True or False.
    """

    my_boolean = False  # Assign either True or False to 'my_boolean'
    return my_boolean

def demonstrate_string():
    """
    This function demonstrates the string data type in Python.
    
    Create a string variable named 'my_string' and assign it any string value.
    A string is a sequence of characters enclosed within single or double quotes.
    """

    # Assign a string value to the variable
    my_string = "Name"
    return my_string

def demonstrate_tuple():
    """
    This function demonstrates the tuple data type in Python.
    
    Create a tuple variable named 'my_tuple' and assign it any tuple value.
    A tuple is an immutable sequence of elements, separated by commas and enclosed within parentheses.
    """

    # Define tuple elements
    element1 = 1
    element2 = 2
    element3 = 3

    # Create the tuple
    my_tuple = tuple((element1, element2, element3))
    
    return my_tuple




def demonstrate_create_areas_list():
    """
    This function creates a list containing the area of the hallway, kitchen, living room,
    bedroom, and bathroom, in the specified order.

    Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), 
    in this order. Use the predefined variables.
    """
    hall = 10
    kit = 20
    liv = 30
    bed = 40
    bath = 15

    areas = [hall, kit, liv, bed, bath]
    
    return areas

def demonstrate_set():
    """
    This function demonstrates the set data type in Python.
    
    Create a set variable named 'my_set' and assign it any set value.
    A set is an unordered collection of unique elements enclosed within curly braces.
    """

    # Define set elements
    element1 = 'a'
    element2 = 'b'
    element3 = 'c'

    # Create the set
    my_set = {element1, element2, element3}
    
    return my_set



def demonstrate_dictionary():
    """
    This function demonstrates the dictionary data type in Python.
    
    Create a dictionary variable named 'my_dict' and assign it any dictionary value.
    A dictionary is a collection of key-value pairs enclosed within curly braces,
    with keys and values separated by a colon.
    """

    # Define dictionary key-value pairs
    key1 = 'key1'
    value1 = 'value1'
    key2 = 'key2'
    value2 = 'value2'

    # Create the dictionary
    my_dict = {
        key1 : value1,
        key2 : value2
    }
    
    return my_dict



def demonstrate_variable_scope():

    """
    This function demonstrates variable scope in Python.
    
    Scope:
    Scope refers to the visibility and accessibility of variables within a program. In Python, variables can have different scopes, 
    which determine where they can be accessed and modified. Understanding variable scope is crucial for writing maintainable and 
    bug-free code.
    
    Local Scope:
    Local scope refers to the scope of variables defined within a particular function or block of code. Variables defined within 
    a function have local scope, meaning they can only be accessed and modified within that function. These variables are not 
    visible to code outside the function and are destroyed once the function completes its execution.
    
    Global Scope:
    Global scope refers to the scope of variables defined outside of any function or block of code. Global variables are accessible 
    and modifiable from anywhere within the program, including within functions. However, when modifying global variables from 
    within a function, it's essential to use the 'global' keyword to explicitly declare that the variable is in the global scope.
    
    
    Instructions:
    1. Observe the error message generated when attempting to print local_var1 inside function1.
    2. Correct the error to successfully print local_var1 inside function1.
    3. Understand the concept of variable scope in Python and how it affects accessing variables inside nested functions.
    """

    # Global variable declaration
    global_var = "I am a global variable"

    def function1():
        """
        This nested function demonstrates variable scope within nested functions.
        
        Challenge:
        Correct the error to print local_var1 inside this function.
        
        Instructions:
        Identify and fix the error preventing the printing of local_var1 inside this function.
        """

        # Local variable declaration within function1
        local_var1 = "I am local to function1"
        
        print("Inside function1 - local_var1: ", local_var1)
        

    function1()  # Call function1 to demonstrate variable scope
    # print("Inside function1 - local_var1:", local_var1)  
    print("Outside function1 - global_var:", global_var)
    return None
