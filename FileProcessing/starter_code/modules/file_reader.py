from modules.exceptions import FileProcessingError, logger

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    for encoding in ['utf-8', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                # Checking if file is empty
                if not file.read():
                    return []
                
                # reset pointer 
                file.seek(0)

                rowData = [] # Initialize list to store row data in
                
                # Get Column Headings
                keys = [cols.strip() for cols in file.readline().split(",")]

                for row in file: # Parse lines/rows in the file
                    vals = [cols.strip() for cols in row.split(",")] # Get list of values for the colums without whitespace
                    rowData.append(dict(zip(keys, vals))) # Trying to match keys (list) to values (list)

            return rowData

        except FileNotFoundError: # Need to log the error before re-raising FileProcessingError?
            logger.error(f"File not found: {filepath}")
            raise FileProcessingError(f"File not found: {filepath}")
        except UnicodeDecodeError as e:
            if encoding == 'latin-1':  # Last attempt failed
                logger.error(f"Encoding failed: {filepath}")
                raise FileProcessingError(f"Could not decode: {filepath}") from e
            logger.warning(f"UTF-8 failed, trying latin-1")