import pandas as pd
from faker import Faker
import random

# Initialize Faker for generating fake data
fake = Faker()

# Number of records to create
num_employees = 100  # Total number of employees
num_departments = 5  # Total number of departments
num_job_titles = 10  # Total number of job titles

# Create data for the Departments table
departments = [{'department_id': i+1, 'department_name': fake.word()} for i in range(num_departments)]
df_departments = pd.DataFrame(departments)  # Convert the list of departments to a DataFrame

# Create data for the Job Titles table
job_titles = [{'job_title_id': i+1, 'job_title': fake.job()} for i in range(num_job_titles)]
df_job_titles = pd.DataFrame(job_titles)  # Convert the list of job titles to a DataFrame

# Create data for the Employees table
employees = []
for i in range(num_employees):
    employee = {
        'employee_id': i+1,  # Unique identifier for each employee
        'name': fake.name(),  # Generate a random name
        'address': fake.address(),  # Generate a random address
        'phone': fake.phone_number(),  # Generate a random phone number
        'email': fake.email(),  # Generate a random email address
        'dob': fake.date_of_birth(minimum_age=18, maximum_age=65),  # Generate a random date of birth
        'job_title_id': random.randint(1, num_job_titles),  # Randomly assign a job title
        'start_date': fake.date_this_decade()  # Generate a random start date within the last decade
    }
    employees.append(employee)  # Append the employee data to the list
df_employees = pd.DataFrame(employees)  # Convert the list of employees to a DataFrame

# Create data for the Salaries table
salaries = []
for i in range(num_employees):
    salary = {
        'salary_id': i+1,  # Unique identifier for each salary record
        'employee_id': i+1,  # Reference to the employee
        'salary_amount': random.randint(40000, 120000),  # Random salary amount between 40,000 and 120,000
        'effective_date': fake.date_this_decade()  # Generate a random effective date within the last decade
    }
    salaries.append(salary)  # Append the salary data to the list
df_salaries = pd.DataFrame(salaries)  # Convert the list of salaries to a DataFrame

# Create data for the Employee_Department table (Many-to-Many relationship)
employee_departments = []
for i in range(num_employees):
    num_depts = random.randint(1, 3)  # Each employee can belong to 1 to 3 departments
    dept_ids = random.sample(range(1, num_departments+1), num_depts)  # Randomly select department IDs
    for dept_id in dept_ids:
        employee_department = {
            'employee_department_id': len(employee_departments) + 1,  # Unique identifier for each employee-department relationship
            'employee_id': i+1,  # Reference to the employee
            'department_id': dept_id  # Reference to the department
        }
        employee_departments.append(employee_department)  # Append the relationship data to the list
df_employee_departments = pd.DataFrame(employee_departments)  # Convert the list to a DataFrame

# Save each DataFrame to a CSV file
df_departments.to_csv('departments.csv', index=False)  # Save Departments data to CSV
df_job_titles.to_csv('job_titles.csv', index=False)  # Save Job Titles data to CSV
df_employees.to_csv('employees.csv', index=False)  # Save Employees data to CSV
df_salaries.to_csv('salaries.csv', index=False)  # Save Salaries data to CSV
df_employee_departments.to_csv('employee_departments.csv', index=False)  # Save Employee_Department data to CSV
