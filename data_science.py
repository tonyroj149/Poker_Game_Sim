import pandas as pd
import matplotlib as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('ds_salaries.csv')

# Retrieve the 'salary' column from the DataFrame
column_data = df[['job_title', 'employment_type']]

# Assign the 'salary' column to test_series
test_series = column_data['salary']

# Define a lambda function that multiplies the input by zero
multiply_by_zero = lambda x: x * 0

# Calculate the correlation between 'job_title' and 'salary' columns
corr = column_data['job_title'].corr(column_data['employment_type'])
print(f'corr: {corr}')

# Apply the lambda function to each element of test_series using map()
# to create a new Series where all values are zero
newseries = test_series.map(multiply_by_zero)

# Print the maximum value in the newseries using the max() method
print(f'Max: {newseries.max()}')
