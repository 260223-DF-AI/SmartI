def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    for record in records: # Iterate through records
        record['total'] = float(f"{(record['quantity'] * record['price']):.2f}") # Create 'total' field for the record and set it to quantity * price

    return records

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    storeSales = {} # Initialize dictionary for stores sales
    for record in records: # Iterate through the records
        if(record['store_id'] not in storeSales): 
            # Record's store_id isn't in storeSales. Set sales for the store to the total in the record
            storeSales[record['store_id']] = record['total']
        else:
            # Record's store_id is in storeSales. Update total, add the record's total
            storeSales[record['store_id']] += record['total']
    
    return storeSales

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    productQuantity = {} # Initialize dictionary for products sales
    for record in records: # Iterate through records
        if(record['product'] not in productQuantity):
            # Record's product isn't in productSales. Set sales (value) for product (key) to quantity in the record
            productQuantity[record['product']] = record['quantity']
        else:
            # Record's product is in productSales. Update total, add the record's quantity
            productQuantity[record['product']] += record['quantity']
    
    return productQuantity