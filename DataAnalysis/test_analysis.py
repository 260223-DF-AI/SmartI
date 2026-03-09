import pytest
import pandas as pd
from starter_code.analysis import *

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        'order_id': [1, 2, 3],
        'customer_id': ['C001', 'C002', 'C001'],
        'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-02']),
        'product_name': ['Widget', 'Gadget', 'Widget'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'quantity': [2, 1, 3],
        'unit_price': [10.00, 25.00, 10.00],
        'region': ['North', 'South', 'North']
    })

def test_clean_data_removes_duplicates(sample_data: pd.DataFrame):
    """Test that clean_data removes duplicate rows."""
    # Add duplicate data
    new = {
        'order_id':1,
        'customer_id':'C001',
        'order_date':pd.to_datetime('2024-01-01'),
        'product_name':'Widget',
        'category':'Electronics',
        'quantity':2,
        'unit_price':10.00,
        'region':'North'}
    sample_data.loc[len(sample_data)] = list(new.values())

    clean_data(sample_data)
    assert [0 for elem in list(sample_data.duplicated()) if elem == True] == []

def test_sales_by_category_calculation(sample_data: pd.DataFrame):
    """Test that category totals are calculated correctly."""
    firstTestData = sample_data.copy()
    clean_data(firstTestData)
    catTotals: pd.DataFrame = sales_by_category(firstTestData)
    assert catTotals['total_sales'].item() == 75.00
    assert catTotals['order_count'].item() == 3
    assert catTotals['avg_order_value'].item() == 25.00

def test_sales_by_category_more_categories(sample_data: pd.DataFrame):
    new = [
        [4, 'C003', pd.to_datetime('2024-01-02'),'Hat', 'Accessories',4,25.00,'East'],
        [5, 'C003', pd.to_datetime('2024-01-06'),'Flip-Flops', 'Shoes',1,5.00,'West'],
        [6, 'C002', pd.to_datetime('2024-01-04'),'T-Shirt', 'Clothes',4,25.00,'South'],
        [7, 'C001', pd.to_datetime('2024-01-03'),'Hairtie', 'Accessories',4,4.50,'North'],
        [8, 'C003', pd.to_datetime('2024-01-05'),'Gadget', 'Electronics',5,40.00,'West'],
        [9, 'C003', pd.to_datetime('2024-01-07'),'Boots', 'Shoes',1,45.00,'East'],
        [10, 'C001', pd.to_datetime('2024-01-04'),'Shorts', 'Clothes',4,30.00,'East'],
        [6, 'C002', pd.to_datetime('2024-01-04'),'T-Shirt', 'Clothes',4,25.00,'South'],
        [8, 'C003', pd.to_datetime('2024-01-05'),'Gadget', 'Electronics',5,40.00,'West'],
    ]
    for row in new:
        sample_data.loc[len(sample_data)] = list(row)
    clean_data(sample_data)
    catTotals: pd.DataFrame = sales_by_category(sample_data)
    total_sale = sample_data.groupby('category', as_index=False).agg(total_sales=('total_amount', 'sum')).sort_values('total_sales', ascending=False)
    assert catTotals['total_sales'].equals(total_sale['total_sales'])

def test_top_products_returns_correct_count(sample_data: pd.DataFrame):
    """Test that top_products returns requested number of items."""
    clean_data(sample_data)
    assert len(list(top_products(sample_data)['product_name'])) == 2
    assert len(list(top_products(sample_data, 1)['product_name'])) == 1

def test_top_products_returns_correct_count_extended(sample_data: pd.DataFrame):
    """Test that top_products returns requested number of items."""
    new = [
        [4, 'C003', pd.to_datetime('2024-01-02'),'Hat', 'Accessories',4,25.00,'East'],
        [5, 'C003', pd.to_datetime('2024-01-06'),'Flip-Flops', 'Shoes',1,5.00,'West'],
        [6, 'C002', pd.to_datetime('2024-01-04'),'T-Shirt', 'Clothes',4,25.00,'South'],
        [7, 'C001', pd.to_datetime('2024-01-03'),'Hairtie', 'Accessories',4,4.50,'North'],
        [8, 'C003', pd.to_datetime('2024-01-05'),'Gadget', 'Electronics',5,40.00,'West'],
        [9, 'C003', pd.to_datetime('2024-01-07'),'Boots', 'Shoes',1,45.00,'East'],
        [10, 'C001', pd.to_datetime('2024-01-04'),'Shorts', 'Clothes',4,30.00,'East'],
        [11, 'C002', pd.to_datetime('2024-01-04'),'T-Shirt', 'Clothes',4,25.00,'South'],
        [12, 'C003', pd.to_datetime('2024-01-05'),'Gadget', 'Electronics',5,40.00,'West'],
    ]
    for row in new:
        sample_data.loc[len(sample_data)] = list(row)
    clean_data(sample_data)
    assert len(list(top_products(sample_data)['product_name'])) == 8
    assert len(list(top_products(sample_data, 5)['product_name'])) == 5
    assert len(list(top_products(sample_data, 0)['product_name'])) == 0

def test_customer_analysis_favorite_category(sample_data: pd.DataFrame):
    """Test that customer_analysis returns correct favorite_category based on total_amount"""
    clean_data(sample_data)
    df: pd.DataFrame = customer_analysis(sample_data)
    assert len(df['favorite_category'].str.fullmatch("Electronics")) == 2

def test_weekend_vs_weekday_sales_percentage(sample_data: pd.DataFrame):
    """Test that the percentage of sales for all the days adds up to 100"""
    clean_data(sample_data)
    add_time_features(sample_data)
    df: pd.DataFrame = weekend_vs_weekday(sample_data)
    assert sum(df['percentages']) == 100.00

def test_weekly_sales_percentages_extended(sample_data: pd.DataFrame):
    new = [
        [4, 'C003', pd.to_datetime('2024-01-02'),'Hat', 'Accessories',4,25.00,'East'],
        [5, 'C003', pd.to_datetime('2024-01-06'),'Flip-Flops', 'Shoes',1,5.00,'West'],
        [6, 'C002', pd.to_datetime('2024-01-04'),'T-Shirt', 'Clothes',4,25.00,'South'],
        [7, 'C001', pd.to_datetime('2024-01-03'),'Hairtie', 'Accessories',4,4.50,'North'],
        [8, 'C003', pd.to_datetime('2024-01-05'),'Gadget', 'Electronics',5,40.00,'West'],
        [9, 'C003', pd.to_datetime('2024-01-07'),'Boots', 'Shoes',1,45.00,'East'],
        [10, 'C001', pd.to_datetime('2024-01-04'),'Shorts', 'Clothes',4,30.00,'East'],
        [11, 'C002', pd.to_datetime('2024-01-04'),'T-Shirt', 'Clothes',4,25.00,'South'],
        [12, 'C003', pd.to_datetime('2024-01-05'),'Gadget', 'Electronics',5,40.00,'West'],
    ]
    for row in new:
        sample_data.loc[len(sample_data)] = list(row)
    clean_data(sample_data)
    add_time_features(sample_data)
    df: pd.DataFrame = weekend_vs_weekday(sample_data)
    assert sum(df['percentages']) > 99.05 and sum(df['percentages']) < 100.05 # rounding and floats means it won't be exactly 100%
