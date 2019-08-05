# Perhaps try this out in ipython!
import pandas

# Simple DataFrame
df1 = pandas.DataFrame([[2,4,6],[10,20,30]])

print(df1)
print(df1.mean()) # mean of each group
print(df1.mean().mean()) # mean of everything

# Possible to add column headers too!
df2 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["ID", "Age", "Price"])

print(df2)
print()
print(df2.Price) # Output only the 'Price' column of data
print(df2.Price.mean()) # Mean of just the Price columnn

# Create a DataFrame from a dict
df3 = pandas.DataFrame([{'first_name': 'Darren', 'last_name': 'Jensen'}, {'first_name': 'Sophia', 'last_name': 'Jensen'}])

print(df3)