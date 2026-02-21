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
- Column selection (e.g., show name, salary)  
- COUNT queries (e.g., count employees)  
- WHERE clause filtering  
- Comparison operators: is, =, >, <, >=, <=, !=  
- Natural inequality: not, is not  
- Range queries using BETWEEN  
- Multiple conditions using AND / OR  
- ORDER BY with ASC/DESC  
- Column validation against schema  
- Automatic handling of numeric and text values  



## Examples
<img width="1082" height="494" alt="image" src="https://github.com/user-attachments/assets/9231f12f-a011-48e7-bfab-d0e27812222e" />
