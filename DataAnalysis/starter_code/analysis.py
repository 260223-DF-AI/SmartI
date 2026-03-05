from numpy import int64, float64
import pandas as pd
from datetime import date

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
    df.drop_duplicates(inplace=True)

    # Drop missing values
    df.dropna(inplace=True)

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
        totals.append(round(quantity * price, 2))
        
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
    # Initialize lists for the columns to be created
    dayOfWeek = [] 
    months = []
    quarters = []
    areWeekends = []

    # Iterate over the df
    for row in df.index:
        # Get the date
        orderDate = date.strptime(str(df.loc[row, 'order_date']).split(" ")[0], "%Y-%m-%d")

        # calculate quarter
        quarter = 0
        if orderDate.month < 4:
            quarter = 1
        elif orderDate.month < 7:
            quarter = 2
        elif orderDate.month < 10:
            quarter = 3
        else:
            quarter = 4

        # Add values to respective lists
        dayOfWeek.append(orderDate.weekday())
        months.append(orderDate.month)
        quarters.append(quarter)
        areWeekends.append(orderDate.weekday() in [5, 6])
    
    # Add columns with data to df
    df['day_of_week'] = dayOfWeek
    df['month'] = months
    df['quarter'] = quarters
    df['is_weekend'] = areWeekends

def sales_by_category(df: pd.DataFrame):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    return df.groupby('category')['total_amount'].agg([
        ('total_sales', 'sum'), 
        ("order_count", 'count'),
        ('avg_order_value', 'mean')]).sort_values('total_sales', ascending=False)

def sales_by_region(df: pd.DataFrame):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    totalSum = float(df['total_amount'].sum())
    byRegionDF = df.groupby('region')['total_amount'].agg([('total_sales', 'sum')])
    byRegionDF['percent_of_total'] = round((byRegionDF['total_sales'] / totalSum) * 100, 2)
    return byRegionDF

def top_products(df: pd.DataFrame, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    # group by products
    return df.groupby('product_name').agg(
        category = ("category", 'first'),
        total_sales = pd.NamedAgg(column='total_amount', aggfunc='sum'),
        units_sold = pd.NamedAgg(column='quantity', aggfunc='sum')
    ).sort_values('total_sales', ascending=False).head(n)

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    pass

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    pass

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    pass

explore_data(load_data("C:/Users/isabe/revature/SmartI/DataAnalysis/starter_code/orders.csv"))
df = load_data("C:/Users/isabe/revature/SmartI/DataAnalysis/starter_code/orders.csv")
clean_data(df)
print(df)
add_time_features(df)
print(sales_by_category(df))
print(sales_by_region(df))
print(top_products(df))