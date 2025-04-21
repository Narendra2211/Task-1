
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Step 2: Display initial info
print("Initial Dataset Info:")
print(df.info())
print("\nFirst 5 Rows:\n", df.head())

# Step 3: Rename columns to lowercase and replace spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 4: Standardize 'gender' column text (capitalize first letter)
df['gender'] = df['gender'].str.strip().str.capitalize()

# Step 5: Check for and remove duplicates
initial_rows = len(df)
df = df.drop_duplicates()
final_rows = len(df)
print(f"\nDuplicates removed: {initial_rows - final_rows}")

# Step 6: Final check of data types and missing values
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

# Step 7: Save the cleaned dataset
df.to_csv("cleaned_mall_customers.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_mall_customers.csv'")
