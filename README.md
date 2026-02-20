# NLP to SQL Converter

This project converts restricted natural language employee queries into SQL SELECT statements for a fixed employee database.

## Database

The system is designed for a dedicated employee table with the following columns:

id, name, department, salary, hire_date, city, age  

Sample data is provided in `database/employees.csv`.

## Run Instructions

Ensure Python is installed, then run:

`python Converter.py`

Enter queries in the console. Type `exit` to quit.

## Project Scope

The converter supports natural language employee retrieval queries and converts them into SQL SELECT statements with optional filtering and sorting.

## Supported Features

- Basic employee listing  
- WHERE clause filtering  
- Comparison operators: is, =, >, <, >=, <=, !=  
- Natural inequality: not, is not  
- Multiple conditions using AND  
- ORDER BY with ASC/DESC  
- Column validation against schema  
- Automatic handling of numeric and text values  



## Examples
<img width="944" height="381" alt="Examples" src="https://github.com/user-attachments/assets/631bc262-2a08-4226-a64e-35930bdc0963" />
