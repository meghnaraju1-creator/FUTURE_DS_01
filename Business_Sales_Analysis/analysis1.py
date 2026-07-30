import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Data/train.csv")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset shape
print("\nShape of Dataset:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Information about the dataset
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Convert Order Date to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
# Check the earliest and latest order dates
print("Date Range:")
print(df["Order Date"].min())
print(df["Order Date"].max())

# Monthly Sales Analysis

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales.head(10))



monthly_sales.plot(figsize=(12,5))

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

#sales by category

category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

#sales by category plot

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

#sales by sub-category

subcategory_sales = df.groupby("Sub-Category")["Sales"].sum()

print(subcategory_sales.sort_values(ascending=False))

#top 10 products by sale

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_products)

#sales by region

region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)

#sales by segment

segment_sales = df.groupby("Segment")["Sales"].sum()

print(segment_sales)

#save cleaned data to a new csv file

df.to_csv("cleaned_dataset.csv", index=False)

#average sales

# Total Sales
total_sales = df["Sales"].sum()

# Total Orders
total_orders = df["Order ID"].nunique()

# Total Customers
total_customers = df["Customer ID"].nunique()

# Average Sales
average_sales = df["Sales"].mean()

print(f"Total Sales: {total_sales:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Average Sales: {average_sales:.2f}")

#state with highest sales

state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(state_sales.head(10))

#plot state sales

plt.figure(figsize=(12,6))
state_sales.head(10).plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

#cities with highest sales

city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(city_sales.head(10))

# Monthly Sales Trend

monthly_sales = df.groupby("Month")["Sales"].sum()

print("Monthly Sales Trend:")
print(monthly_sales)

monthly_sales.plot(
    kind="line",
    figsize=(10,5),
    marker="o",
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

