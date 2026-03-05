from numpy import int64, float64
import pandas as pd

def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    try:
        # Load data into a dataframe
        orders: pd.DataFrame = pd.read_csv(filepath, 
            date_format="%Y-%m-%d", parse_dates=['order_date'], # Parse dates
            na_values=None) # Handle missing values

        print(orders.head())
        return orders # Return clean dataframe
    except Exception as e:
        print(e)

def explore_data(df: pd.DataFrame):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    # Print shape
    print(f"Shape: {df.shape}\n")

    # Print data types
    print(f"Data types:\n{df.dtypes}\n")

    # Print missing value counts: total missing value elements = total elements - total non-null elements
    print(f"Total missing value count: {(df.size - df.count().sum())}\n")

    # Print basic statistics for numeric columns (I didn't include order_id)
    # Create a list of the names of colums that store numeric data excluding the order_id
    numCols = [col for col in df.columns if df[col].dtype in [int64, float64]][1:]
    # How do I format the floats?
    print(f"Stats for numeric columns:\n{df[numCols].describe()}\n")

    # Print date range covered
    print(f"Date range: {df['order_date'].min()} to {df['order_date'].max()}")

def clean_data(df: pd.DataFrame):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    # Remove duplicates
    df.drop_duplicates()

    # Drop missing values
    df.dropna()

    ## Standardize text columns

    # Finding headings for columns that store strings
    strCols = [col for col in df.columns if df[col].dtype == 'str']

    totals = [] # for 'total_ammount's

    # iterate through df
    for row in df.index:

        # Give consistent casing (I don't like what it did to the acronym)
        df.loc[row, strCols] = df[strCols].loc[row].str.title()

        # Remove whitespace
        df.loc[row, strCols] = df[strCols].loc[row].str.strip()

        # Add calculated 'total_amount' columns
        quantity = int(df.loc[row, 'quantity'])
        price = float(df.loc[row, 'unit_price'])
        totals.append(float(str(f"{(quantity * price):.2f}")))
        
    # Add new 'total_amount' column with values
    df['total_amount'] = totals

def add_time_features(df: pd.DataFrame):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    pass

explore_data(load_data("C:/Users/isabe/revature/SmartI/DataAnalysis/starter_code/orders.csv"))
df = load_data("C:/Users/isabe/revature/SmartI/DataAnalysis/starter_code/orders.csv")
clean_data(df)
print(df)