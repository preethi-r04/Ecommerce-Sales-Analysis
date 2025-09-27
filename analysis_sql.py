import sqlite3
import pandas as pd

# -------------------------------
# Step 1: Load CSV
# -------------------------------
df = pd.read_csv("indian_ecommerce_sales.csv")

# -------------------------------
# Step 2: Connect to SQLite
# -------------------------------
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# -------------------------------
# Step 3: Load CSV into SQL table
# -------------------------------
df.to_sql('orders', conn, if_exists='replace', index=False)
print("Dataset loaded into SQL successfully!\n")

# -------------------------------
# Step 4: SQL Queries for KPIs
# -------------------------------

# 1️⃣ Total Sales, Profit, Avg Order Value
query1 = """
SELECT 
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND(SUM(sales)/COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM orders;
"""
result1 = pd.read_sql(query1, conn)
print("Total Sales, Profit & Avg Order Value:")
print(result1, "\n")

# 2️⃣ Sales & Profit by Region
query2 = """
SELECT 
    region, 
    SUM(sales) AS total_sales, 
    SUM(profit) AS total_profit
FROM orders
GROUP BY region
ORDER BY total_sales DESC;
"""
result2 = pd.read_sql(query2, conn)
print("Sales & Profit by Region:")
print(result2, "\n")

# 3️⃣ Top 5 Products by Sales
query3 = """
SELECT 
    product_id, 
    SUM(sales) AS total_sales
FROM orders
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 5;
"""
result3 = pd.read_sql(query3, conn)
print("Top 5 Products by Sales:")
print(result3, "\n")

# 4️⃣ Monthly Sales Trend
query4 = """
SELECT 
    order_month, 
    SUM(sales) AS monthly_sales
FROM orders
GROUP BY order_month
ORDER BY order_month;
"""
result4 = pd.read_sql(query4, conn)
print("Monthly Sales Trend:")
print(result4, "\n")

# 5️⃣ Payment Method Distribution
query5 = """
SELECT 
    payment_method, 
    COUNT(*) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;
"""
result5 = pd.read_sql(query5, conn)
print("Payment Method Distribution:")
print(result5, "\n")


conn.close()
print("SQL connection closed.")
