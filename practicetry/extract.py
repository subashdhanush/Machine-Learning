import pandas as pd

df = pd.read_excel('students.xlsx',header=None)
df.columns = df.columns.str.strip()
print("df",df)
filtered = df[df['Score'] > 80]
print(filtered)
# filtered.to_excel('top_students.xlsx', index=False)
