import pandas as pd

# Load an example dataset
df1 = pd.read_csv('media_views.csv', low_memory=False)
df2 = pd.read_csv('page_views.csv', low_memory=False)

# Print the shape of the datasets

print("media_views CSV saved. Shape:", df1.shape)
print("page_views CSV saved. Shape:", df2.shape)

# Inspect column names
print("Columns in df1:", df1.columns.tolist())
print("Columns in df2:", df2.columns.tolist())

# Harmonize column names as necessary, for example:
df2.rename(columns={'old_name': 'new_name'}, inplace=True)

# Optionally, drop irrelevant columns
# df1.drop(['unnecessary_column'], axis=1, inplace=True)
# df2.drop(['unnecessary_column'], axis=1, inplace=True)

# Merge datasets
merged_df = pd.merge(df1, df2, on='student_id', how='outer')

# Handling duplicates after merge (if necessary)
merged_df.drop_duplicates(inplace=True)

# Save the merged dataset
merged_df.to_csv('merged_data.csv', index=False)

print("Merged CSV saved. Shape:", merged_df.shape)
