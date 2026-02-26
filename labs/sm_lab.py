# Good to go


def get_string_length(s):
    """
    
    Instead of returning 0, this method should return  the length of a string.
    
    :param s: The string to be manipulated.
    :return: The length of the string.
    """
    return len(s)

def get_character_at_index(s, n):
    """
    Instead of returning a null character, this method should return the character of a string at a specific index.
    
    :param s: The string to be manipulated.
    :param n: An index of the string.
    :return: The character of the string at the specified index.
    """
    return s[n]

def get_index_given_character(s, c):
    """
    Instead of returning 0, this method should return the index of the first occurrence of a character within a string.
    Returns -1 if the character does not exist in the string.
    
    :param s: The string to be manipulated.
    :param c: A character within the string.
    :return: The index of the first occurrence of the character within the string.
    """
    if c == '':
        return -1
    return s.find(c)

def string_slicing(s, start, end):
    """
    Instead of returning null string, this method should Slice a string to extract a substring and return it.
    
    :param s: The string to be manipulated.
    :param start: The starting index of the slice.
    :param end: The ending index of the slice.
    :return: The sliced substring.
    """
    return s[start:end + 1]  # Adjust end index to be inclusive





def concatenate_strings(string1, string2):
    """
    Instead of returning the null string, this method should
    Concatenates two strings with a space in between.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        str: The concatenated string with a space in between.

    Example:
        string1: "Good"
        string2: "morning"
        return: "Good morning"
    """
    return string1 + " " + string2

def repeat_string(s, times):
    """
    Instead of returning null string, this method should returnRepeat a string multiple times.
    
    :param s: The string to be repeated.
    :param times: The number of times to repeat the string.
    :return: The repeated string.
    """
    return s*times

def string_length(s):
    """
    Instead of returning 0, this method should return the length of a string.
    
    :param s: The string to get the length of.
    :return: The length of the string.
    """
    return len(s)

def convert_to_uppercase(s):
    """
    Instead of returning null string, this method should return a string in uppercase.
    
    :param s: The string to be converted.
    :return: The uppercase version of the string.
    """
    return s.upper()

def convert_to_lowercase(s):
    """
    Instead of returning null string, this method should return the string in lowercase.
    
    :param s: The string to be converted.
    :return: The lowercase version of the string.
    """
    return s.lower()