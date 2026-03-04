from datetime import datetime

def write_summary_report(filepath, valid_records, errors, aggregations):
    """
    Write a formatted summary report.

    Report should include:
    - Processing timestamp
    - Total records processed
    - Number of valid records
    - Number of errors (with details)
    - Sales by store
    - Top 5 products
    """
    # I know this isn't the way I was intended to do this, but I am already over halfway through doing it this way

    reportTimestamp = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

    # Opening of the report
    lines = ["=== Sales Processing Report ==="]
    lines.append(f"Generated: {reportTimestamp}\n")

    # Processing statistics
    lines.append("Processing statistics:")
    lines.append(f"- Total records: {len(valid_records) + len(errors)}")
    lines.append(f"- Valid records: {len(valid_records)}")
    lines.append(f"- Error records: {len(errors)}\n")

    # Display errors
    lines.append("Errors:")
    for error in errors:
        lines.append(f"- {error}")
    lines.append("\n")

    # Sales Statistics
    lines.append("Sales by Store:")
    stores = aggregations[0]
    for store in stores:
        lines.append(f"- {store}: ${stores[store]:.2f}")
    lines.append("\n")

    # Product Statistics
    lines.append("Top Products:")
    products = aggregations[1]
    i = 0
    for i, product in enumerate(products):
        if(i < 5):
            lines.append(f"{i+1}. {product}: {products[product]} units")
        else:
            break

    reportText = "\n".join(lines)

    try:
        with open(filepath, "w") as file:
            file.write(reportText)
    except Exception as e:
        print(e)
    
    

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    cleanedRecords = ",".join(list(records[0].keys())) + "\n"
    for record in records:
        cleanedRecords += ",".join([str(val) for val in record.values()]) + "\n"
    try:
        with open(filepath, "w") as file:
            file.write(cleanedRecords)
    except Exception as e:
        print(e)

def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    errorsString = ""
    for error in errors:
        errorsString += str(error) + "\n"
    try:
        with open(filepath, "a") as file:
            file.write(errorsString)
    except Exception as e:
        print(e)
