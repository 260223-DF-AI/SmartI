from math import ceil
def read_lines(filepath, encoding='utf-8'):
    """
    Yield lines from a file one at a time.
    - Strip whitespace from each line
    - Skip empty lines
    - Handle encoding errors gracefully
    
    Usage:
        for line in read_lines('large_file.txt'):
            process(line)
    """
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            for line in file:
                line = line.strip()
                if len(line) > 0:
                    yield line
    except UnicodeEncodeError:
        print("Error caused by improper encoding selection.")
        exit(-1) # is exit(-1) considered handling it gracefully?

def batch(iterable, size):
    """
    Yield items in batches of the specified size.
    
    Usage:
        list(batch([1,2,3,4,5,6,7], 3))
        # [[1,2,3], [4,5,6], [7]]
    """
    start = 0
    end = start + size + 1
    for i in range(ceil(len(iterable) / size)):
        if(len(iterable) - start < end): # make sure I am not trying to access indecies that don't exist
            end = len(iterable)
        yield iterable[start:end]

        # increment my values
        start = end
        end += size + 1

def filter_by(iterable, predicate):
    """
    Yield items that match the predicate.
    
    Usage:
        evens = filter_by(range(10), lambda x: x % 2 == 0)
        list(evens)  # [0, 2, 4, 6, 8]
    """
    for i in iterable:
        if predicate(i):
            yield i

def filter_errors(log_lines):
    """
    Yield only lines containing 'ERROR'.
    """
    for line in log_lines:
        if "ERROR" in line:
            yield line

def filter_by_field(records, field, value):
    """
    Yield records where record[field] == value.
    
    Usage:
        active_users = filter_by_field(users, 'status', 'active')
    """
    for record in records:
        if record[field] == value:
            yield record