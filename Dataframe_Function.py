'''
A function that takes in DataFrame and check if it has a Sales and website traffic columns.

The function should divide those two and return if the conversion rate is going up or down
'''
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sample_data import sales_data

def check_data(data):
    # Checking for sales column
    if 'Sales_Quantity' not in data:
        print("No sales column found")
        return False
    # Checking for website traffic column
    elif 'Website_Traffic' not in data:
        print("No Website Traffic column found")
        return False
    else:
        # Calculating Conversion Rate
        conv_rate = (data['Sales_Quantity'] / data['Website_Traffic']) * 100
        # Returning result
         # Checking the change in conversion rate
        change = conv_rate.diff()
        if change.dropna().gt(0.5).all():
            return "Conversion rate is going up"
        elif change.dropna().lt(0.5).all():
            return "Conversion rate is going down"
        else:
            return "Conversion rate remains same"
        

## Create dataframe from sales data
df = pd.DataFrame(sales_data)

# Plotting Sales vs. Traffic using Seaborn
sb.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sb.lineplot(data=df[['Sales_Quantity', 'Website_Traffic']])
plt.xlabel('Months')
plt.ylabel('Amount in USD')
plt.title('Sales and Traffic Over Time')

# Get the unique month names from the 'Month' column
month_names = df['Month'].unique()
amount = df['Sales_Quantity'].unique()

# Set x-axis tick locations and labels
plt.xticks(ticks=range(len(month_names)), labels=month_names, rotation=45)



plt.tight_layout()
plt.show()


result = check_data(df)
print(result)
