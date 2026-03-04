from datetime import date
from modules.exceptions import InvalidDataError, MissingFieldError

def validate_sales_record(record, line_number):
    """
    Validate a single sales record.
    
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number
    
    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError
    """
    # Check for empty fields
    for field in ['date', 'store_id', 'product', 'quantity', 'price']:
        if field not in record or not record[field]:
            raise MissingFieldError(f"Line {line_number}: Missing required field '{field}'")
    
    # Check date format
    try:
        date.strptime(record['date'], "%Y-%m-%d")
    except ValueError:
        raise InvalidDataError(f"Line {line_number}: Invalid date format '{record['date']}'")
    
    # Check quantity (positive int)
    try:
        quantity = int(record['quantity'])

        if quantity < 1: # Check if quantity is 0 or a negative integer
            raise InvalidDataError(f"Line {line_number}: Quantity must be a positive integer, got {record['quantity']}")
        record['quantity'] = quantity
    except ValueError:
        raise InvalidDataError(f"Line {line_number}: Quantity must be a positive integer, got {record['quantity']}")

    # Check price (positive numerical value)
    try:
        price = float(record['price'])

        if price <= 0.0: # Check if the value of price is positive
            raise InvalidDataError(f"Line {line_number}: Price must be a positive number, got {record['price']}")
        record['price'] = price
    except ValueError:
        raise InvalidDataError(f"Line {line_number}: Price must be a positive number, got {record['price']}")

    return record

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    valid_records = [] # Initialize a list for valid records
    error_list = [] # Initialize a list for errors
    for i, record in enumerate(records): # Parse the records
        try: # Try to validate and add a record to valid_records
            valid_records.append(validate_sales_record(record, i)) 
        except MissingFieldError as e: # Catch MissingFieldError
            error_list.append(e) # add exception message to the list of errors
        except InvalidDataError as e: # Catch InvalidDataError
            error_list.append(e) # add exception message to the list of errors
    
    return (valid_records, error_list)
