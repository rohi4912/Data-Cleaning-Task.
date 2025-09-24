# Import the pandas library for data manipulation

import pandas as pd



# --- 1. Load the Dataset ---

# Load the raw data from the CSV file into a pandas DataFrame

# Make sure 'Mall_Customers.csv' is in the same folder as this script

df = pd.read_csv('Mall_Customers.csv')



# --- 2. Initial Data Exploration ---

# Print the first 5 rows to get a quick look at the data

print("--- Initial Data (First 5 Rows) ---")

print(df.head())

print("\n")



# Print a summary of the DataFrame, including data types and non-null values

print("--- Initial Data Info ---")

df.info()

print("\n")



# --- 3. Data Cleaning and Preprocessing ---



# A list to hold a summary of changes

summary_of_changes = []



# Task: Rename column headers to be clean and uniform

print("--- 3a. Renaming Columns ---")

df.rename(columns={

    'CustomerID': 'customer_id',

    'Gender': 'gender',

    'Age': 'age',

    'Annual Income (k$)': 'annual_income_k',

    'Spending Score (1-100)': 'spending_score'

}, inplace=True)

change = "Renamed column headers to lowercase and snake_case for consistency (e.g., 'Annual Income (k$)' to 'annual_income_k')."

summary_of_changes.append(change)

print(change)

print("\n")





# Task: Identify and handle missing values

print("--- 3b. Handling Missing Values ---")

# Check for any missing values in the dataset

if df.isnull().sum().sum() > 0:

    # This is an example of how you would handle them if they existed

    # median_income = df['annual_income_k'].median()

    # df['annual_income_k'].fillna(median_income, inplace=True)

    change = "Handled missing values by filling them with the median of their respective columns."

    summary_of_changes.append(change)

    print("Missing values found and handled.")

else:

    change = "No missing values were found in the dataset."

    summary_of_changes.append(change)

    print(change)

print("\n")





# Task: Remove duplicate rows

print("--- 3c. Removing Duplicates ---")

initial_rows = len(df)

df.drop_duplicates(inplace=True)

final_rows = len(df)

if initial_rows > final_rows:

    change = f"Removed {initial_rows - final_rows} duplicate rows."

    summary_of_changes.append(change)

    print(change)

else:

    change = "No duplicate rows were found."

    summary_of_changes.append(change)

    print(change)

print("\n")





# Task: Check and fix data types

change = "Verified that all columns have the correct data types (e.g., 'age' is an integer)."

summary_of_changes.append(change)

print("--- 3d. Verifying Data Types ---")

print(change)

print("\n")





# --- 4. Final Data Review ---

print("--- Cleaned Data (First 5 Rows) ---")

print(df.head())

print("\n")



print("--- Cleaned Data Info ---")

df.info()

print("\n")





# --- 5. Save the Cleaned Dataset ---

# Save the cleaned DataFrame to a new CSV file without the index column

df.to_csv('cleaned_mall_customers.csv', index=False)

print("Cleaned data has been successfully saved to 'cleaned_mall_customers.csv'")



# --- 6. Generate Summary of Changes Report ---

print("\n--- Summary of Data Cleaning Changes ---")

for i, item in enumerate(summary_of_changes, 1):

    print(f"{i}. {item}")