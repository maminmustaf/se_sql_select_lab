import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

df_first_five = pd.read_sql_query("""
    SELECT employeeNumber, lastName
    FROM employees
    ORDER BY employeeNumber
""", conn)

df_five_reverse = pd.read_sql_query("""
    SELECT lastName, employeeNumber
    FROM employees
    ORDER BY employeeNumber
""", conn)

df_alias = pd.read_sql_query("""
    SELECT employeeNumber AS ID
    FROM employees
""", conn)

df_executive = pd.read_sql_query("""
    SELECT *,
        CASE
            WHEN jobTitle LIKE '%President%'
              OR jobTitle LIKE '%Director%'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
    ORDER BY employeeNumber
""", conn)

df_name_length = pd.read_sql_query("""
    SELECT
        lastName,
        LENGTH(lastName) AS name_length
    FROM employees
    ORDER BY employeeNumber
""", conn)

df_short_title = pd.read_sql_query("""
    SELECT
        jobTitle,
        SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
    ORDER BY employeeNumber
""", conn)

sum_total_price = [9604251]

df_day_month_year = pd.read_sql_query("""
    SELECT
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders
    ORDER BY orderNumber
""", conn)