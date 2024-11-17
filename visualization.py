import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('sales_data.csv')

# Convert 'Quarter' to a categorical type for ordering in the charts
df['Quarter'] = pd.Categorical(df['Quarter'], categories=["Q1", "Q2", "Q3", "Q4"], ordered=True)

# Set style for plots
sns.set(style="whitegrid")

# 1. Bar Chart for Revenue by Territory
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Territory', y='Revenue_Amount', ci=None, palette='viridis')
plt.title('Total Revenue by Sales Territory')
plt.xlabel('Territory')
plt.ylabel('Revenue Amount ($)')
plt.xticks(rotation=45)
plt.show()

# 2. Line Chart for Actual vs Forecasted Revenue by Quarter
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Quarter', y='Revenue_Amount', hue='Territory', marker='o', label="Actual Revenue")
sns.lineplot(data=df, x='Quarter', y='Forecasted_Revenue', hue='Territory', marker='o', linestyle='--', label="Forecasted Revenue")
plt.title('Actual vs Forecasted Revenue by Quarter and Territory')
plt.xlabel('Quarter')
plt.ylabel('Revenue Amount ($)')
plt.legend(loc='upper left')
plt.show()

# 3. KPI Cards for Key Metrics
total_revenue = df['Revenue_Amount'].sum()
total_forecasted_revenue = df['Forecasted_Revenue'].sum()
total_customers = df['Customer_Count'].nunique()

print("KPI Metrics:")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Forecasted Revenue: ${total_forecasted_revenue:,.2f}")
print(f"Distinct Customers: {total_customers}")

# 4. Trend Table (Pivot Table) of Revenue and Customer Counts by Quarter and Territory
trend_table = df.pivot_table(index='Quarter', columns='Territory', values=['Revenue_Amount', 'Customer_Count'], aggfunc='sum')
print("\nRevenue and Customer Trend Table:")
print(trend_table)
