
# asked in hackerrank for teck company
import pandas as pd

# Sample data with two employees and multiple rows
data = {
    'employee_id': [101, 101, 102, 102, 101, 101, 102, 102],
    'branch_code': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
    'sales': [9000, 8500, 8000, 9000, 9500, 8500, 8000, 9500]
}

# Create DataFrame
df = pd.DataFrame(data)

# Step 1: Find the employee with the highest sales for each branch
branch_max_sales = df.groupby(['branch_code', 'employee_id'], as_index=False)['sales'].sum()
print(branch_max_sales)
branch_top_employees = branch_max_sales.loc[branch_max_sales.groupby('branch_code')['sales'].idxmax()]

print("branch", branch_top_employees)

# Step 2: Check if a single employee has the highest sales across all branches
unique_top_employees = branch_top_employees['employee_id'].nunique()
print("unique",unique_top_employees)

if unique_top_employees == 1:
    # If one employee has the highest sales across all branches, return their ID
    result_df = branch_top_employees[['employee_id']].drop_duplicates()
else:
    # If there is a tie, return an empty DataFrame
    result_df = pd.DataFrame()

print(result_df)
