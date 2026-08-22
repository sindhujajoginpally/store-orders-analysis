import pandas as pd  # imports the pandas library, nicknamed pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

print(orders.info())
print(customers.info())

print(orders.describe())
print(customers.describe())


orders_cleaned = orders.dropna()  # creates a separate copy with ALL rows containing any missing value removed (not actually used later)

orders["CustomerID"] = orders["CustomerID"].fillna("Unknown")  # fills missing Customer Name values with the text "Unknown"
orders["Quantity"] = orders["Quantity"].fillna(orders["Quantity"].mode()[0])  # fills missing Quantity values with the most common quantity in the column

orders["CustomerID"] = orders["CustomerID"].str.strip()  # removes extra leading/trailing spaces from every name
orders["Product"] = orders["Product"].str.lower()  # converts every product name to lowercase, so casing differences don't count as different products

orders["OrderDate"] = pd.to_datetime(orders["OrderDate"], format="mixed")  # converts the Order Date column from text into real dates, handling multiple date formats
print(orders["OrderDate"])  # prints the cleaned, standardized dates

customers["CustomerName"] = customers["CustomerName"].str.strip()  # removes extra leading/trailing spaces from every name

print(orders.isnull().sum())
print(orders["Product"].unique())
print(orders["OrderDate"])
print(customers["CustomerName"].unique())

merged = orders.merge(customers, on="CustomerID")
print(merged)

merged["Total"] = merged["Quantity"] * merged["UnitPrice"]
print(merged)

print(merged["Total"].sum())  # prints the overall total revenue (sum of the Total column across all rows)

city_revenue = merged.groupby("City")["Total"].sum()  # groups rows by City, then sums the Total column within each city group
print(city_revenue)  # prints total revenue per city, in whatever order cities appear
print(city_revenue.sort_values(ascending=False))  # prints total revenue per city, sorted in descending order

customer_spend = merged.groupby("CustomerName")["Total"].sum().sort_values(ascending=False)
print(customer_spend)

print(merged.groupby("Segment")["Total"].mean())