import pyodbc
import pandas as pd

# Function to read connection string information from a file
def get_connection_string(file_path='config/info_db.txt'):
    with open(file_path, 'r') as f:
        return f.read().strip()  # Return the connection string without leading/trailing whitespace

# Connect to SQL Server using the connection string
conn_str = get_connection_string()  # Retrieve the connection string from the file
conn = pyodbc.connect(conn_str)  # Establish the connection
cursor = conn.cursor()  # Create a cursor object for executing SQL commands

# Function to load data from a DataFrame into the specified SQL Server table
def load_data(table_name, df):
    for _, row in df.iterrows():  # Iterate through each row in the DataFrame
        columns = ', '.join(row.index)  # Join the column names into a string
        placeholders = ', '.join(['?'] * len(row))  # Create placeholders for SQL insertion
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"  # Construct the SQL insert statement
        cursor.execute(sql, *row)  # Execute the SQL statement with the row data
    conn.commit()  # Commit the transaction to save changes in the database

# Read the CSV files into DataFrames
df_departments = pd.read_csv('departments.csv')  # Load Departments data from CSV
df_job_titles = pd.read_csv('job_titles.csv')  # Load Job Titles data from CSV
df_employees = pd.read_csv('employees.csv')  # Load Employees data from CSV
df_salaries = pd.read_csv('salaries.csv')  # Load Salaries data from CSV
df_employee_departments = pd.read_csv('employee_departments.csv')  # Load Employee_Department data from CSV

# Load data from each DataFrame into the corresponding SQL Server tables
load_data('Departments', df_departments)  # Load Departments data into the SQL Server table
load_data('Job_Titles', df_job_titles)  # Load Job Titles data into the SQL Server table
load_data('Employees', df_employees)  # Load Employees data into the SQL Server table
load_data('Salaries', df_salaries)  # Load Salaries data into the SQL Server table
load_data('Employee_Department', df_employee_departments)  # Load Employee_Department data into the SQL Server table

# Close the connection to the SQL Server
conn.close()  # Properly close the connection to free resources
