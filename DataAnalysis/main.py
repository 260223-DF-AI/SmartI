from starter_code.analysis import *
from starter_code.visualizations import *

# inPath = "C:/Users/isabe/revature/SmartI/DataAnalysis/starter_code/orders.csv"
# outPath = "C:/Users/isabe/revature/SmartI/DataAnalysis/output/"
def main():
    # get paths
    inPath = input("Enter path to csv data: ")
    outPath = input("Enter path to directory to store figures in: ")
    
    # load data into pandas and prepare it
    df = load_data(inPath)
    clean_data(df)
    add_time_features(df)

    # run analyses
    categorySales = sales_by_category(df)
    print(f"Sales by Category:\n{categorySales}\n")
    regionSales = sales_by_region(df)
    print(f"Sales by Region:\n{regionSales}\n")
    topProducts = top_products(df)
    print(f"Top Products (up to 10):\n{topProducts}\n")
    sales = daily_sales_trend(df)
    print(f"Daily Sales Trends:\n{sales}\n")
    customerAnalysis = customer_analysis(df)
    print(f"Customer Sales Analysis:\n{customerAnalysis}\n")
    weekendVsWeekday = weekend_vs_weekday(df)
    print(f"Weekend Sales vs Weekday Sales:\n{weekendVsWeekday}\n")

    # matplotlib data visualizations
    create_category_bar_chart(categorySales, f"{outPath}categoryBarChart.png")
    create_regional_pie_chart(regionSales, f"{outPath}regionalPieChart.png")
    create_sales_trend_line(sales, f"{outPath}salesTrendLine.png")

    createTopProductsHBarChart(topProducts)

    # Data information
    explore_data(df)