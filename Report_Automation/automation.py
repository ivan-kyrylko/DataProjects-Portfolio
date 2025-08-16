import pandas as pd

df = pd.read_csv('input.csv')
df.to_excel('output.xlsx', index=False)
print("Report exported to Excel")
