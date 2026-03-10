import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import ceil

def create_category_bar_chart(category_data: pd.DataFrame, output_path):
    """
    Create a horizontal bar chart of sales by category.
    - Include value labels on bars
    - Use a professional color scheme
    - Save to output_path
    """
    # data has: category, total sales, order count, average order value
    # Y-axis: category (Bars: total sales, average order value)
    # X-axis: price
    categories = category_data['category']
    sales = {
        'Total Sales': category_data['total_sales'].to_list(),
        'Average Order Value': category_data['avg_order_value'].to_list()
    } 

    category_labels = np.arange(len(categories))

    fig, ax = plt.subplots()

    height = 0.25
    multiplier = 0
    max_val = max(category_data['total_sales'].to_list() + category_data['avg_order_value'].to_list())

    for col, value in sales.items():
        offset = height * multiplier
        bar = ax.barh(category_labels + offset, value, height, label=col)
        ax.bar_label(bar, padding=5)
        multiplier += 1
    
    ax.set_title("Sales By Category")
    ax.set_xlabel("USD ($)")
    ax.set_yticks(category_labels + (height / 2), categories)
    ax.legend(loc='upper right', ncols=2)
    ax.set_xlim(0, ceil(max_val) + 50)
    
    plt.tight_layout()
    plt.show()

def create_regional_pie_chart(region_data: pd.DataFrame, output_path):
    """
    Create a pie chart showing sales distribution by region.
    - Include percentages
    - Use distinct colors for each region
    - Save to output_path
    """
    regions = region_data['region']
    percentages = region_data['percent_of_total']

    plt.pie(percentages, labels=regions, autopct="%1.1f%%")

    plt.title("Sales by Region")
    plt.show()

def create_sales_trend_line(daily_data: pd.DataFrame, output_path):
    """
    Create a line chart showing daily sales trend.
    - Include moving average (7-day)
    - Mark weekends differently
    - Add proper axis labels and title
    - Save to output_path
    """
    # daily_data: DataFrame with columns [date, total_sales, order_count]
    # Make a copy to avoid modifying the original
    df = daily_data.copy()
    
    # Sort by date
    df = df.sort_values('date')
    df['date'] = pd.to_datetime(df['date']).dt.normalize()

    # Calculate 7-day moving average
    df['weekly_avg'] = df['total_sales'].rolling(window=7, min_periods=1).mean()
    
    # Create the plot
    fig, ax = plt.subplots()
    
    # Plot the main sales line
    df['is_weekend'] = df['date'].dt.dayofweek >= 5
    ax.plot(df['date'], df['total_sales'],
            label='Daily Sales', 
            color='#2E86AB', marker='o',
            linewidth=1.5, alpha=0.7)
    weekendDF = df[df['is_weekend']]
    ax.plot(weekendDF['date'], weekendDF['total_sales'], color='purple', marker='o', linestyle="")
    # Plot the moving average
    ax.plot(df['date'], df['weekly_avg'], label='7-Day Moving Average', marker='o', linewidth=2, linestyle='--')
    
    # Formatting
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Sales ($)')
    ax.set_title('Daily Sales Trend')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()

def createTopProductsHBarChart(df: pd.DataFrame) -> plt:
    product_names = df['product_name']
    sales = df['total_sales']
    
    fig, ax = plt.subplots()
    
    # Create horizontal bar chart
    bars = ax.barh(product_names, sales)
    
    # Add value labels on bars
    ax.bar_label(bars, padding=5, fmt='$%.0f')
    
    # Formatting
    ax.set_xlabel('Total Sales ($)')
    ax.set_ylabel('Product')
    ax.set_title('Top 10 Products by Sales')
    
    plt.tight_layout()
    plt.show()

def create_dashboard(df: pd.DataFrame, output_dir):
    """
    Create a multi-panel dashboard with 4 subplots:
    1. Sales by category (bar)
    2. Sales by region (pie)
    3. Daily trend (line)
    4. Top 10 products (horizontal bar)
    Save as a single figure.
    """
    create_category_bar_chart(df, "")
    create_regional_pie_chart(df, "")
    create_sales_trend_line(df, "")
    pass