from modules.exceptions import FileProcessingError
from modules.file_reader import read_csv_file
from modules.report_writer import *
from modules.transformer import *
from modules.validator import validate_all_records

# input_path: string, path to sample_sales.csv
# output_dir: string, path to starter_code
def process_sales_file(input_path, output_dir):
    """
    Main processing pipeline.
    
    1. Read the input file
    2. Validate all records
    3. Transform valid records
    4. Generate reports
    5. Handle any errors gracefully
    
    Returns: ProcessingResult with statistics
    """
    try:
        # read input file
        recordDicts: list = read_csv_file(input_path)

        # validate all records
        records: tuple = validate_all_records(recordDicts)

        # transform valid records
        calculate_totals(records[0])
        salesStore: dict = aggregate_by_store(records[0])
        productQuantity: dict = aggregate_by_product(records[0])

        # generate reports
        write_summary_report(output_dir + "sales_report.txt", records[0], records[1], [salesStore, productQuantity])
        write_clean_csv(output_dir + "clean_csv.csv", records[0])
        write_error_log(output_dir + "errorLog.txt", records[1])
    except FileProcessingError as e:
        print(f"File processing error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Process from command line
    inputPath = input("Enter path to input data file: ")
    outputDir = input("Enter path to directory for output files: ")

    try:
        process_sales_file(inputPath, outputDir)
        print("Completed. Success!")
    except Exception as e:
        print(f"Error: {e}")