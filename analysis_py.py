import pandas as pd

# Load dataset
df = pd.read_csv("indian_ecommerce_sales.csv")

# Check first rows
print(df.head())

# Missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates(subset='order_id')

# Convert order_date
df['order_date'] = pd.to_datetime(df['order_date'])

# Create month_year
df['month_year'] = df['order_date'].dt.to_period('M').astype(str)

# Total sales & profit
print("Total Sales:", df['sales'].sum())
print("Total Profit:", df['profit'].sum())

# Sales by Category
print(df.groupby('category')['sales'].sum().sort_values(ascending=False))

#Sales by Region
sales_by_region = df.groupby('region')['sales'].sum().sort_values(ascending=False)
print(sales_by_region)

#Profit by Category
profit_by_category = df.groupby('category')['profit'].sum().sort_values(ascending=False)
print(profit_by_category)

#Top 5 Products by Sales
top_products = df.groupby('product_id')['sales'].sum().sort_values(ascending=False).head(5)
print(top_products)

#Monthly Sales Trend
monthly_sales = df.groupby('order_month')['sales'].sum()
print(monthly_sales)

#Payment Method Analysis
payment_counts = df['payment_method'].value_counts()
print(payment_counts)


