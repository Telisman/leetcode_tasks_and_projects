'''
    Table: Employee
    Column Name | Type |
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.


Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
'''

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Check if the 'Salary' column exists in the DataFrame
    if 'salary' not in employee.columns:
        raise ValueError("The 'salary' column does not exist in the DataFrame.")

    # Remove duplicate salaries to handle cases where multiple employees have the same salary
    unique_salaries = employee['salary'].unique()

    # Check if there are at least two unique salaries
    if len(unique_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    # Sort the unique salaries in descending order and select the second one
    unique_salaries.sort()
    second_highest = unique_salaries[-2]

    return pd.DataFrame({'SecondHighestSalary': [second_highest]})