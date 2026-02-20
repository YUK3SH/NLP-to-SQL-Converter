def parse_nlp_to_sql(user_input):
    user_input = user_input.lower().strip()

    valid_columns = ["id", "name", "department", "salary", "hire_date", "city"]

    if not user_input.startswith("show employees"):
        return "Error: command should start with 'show employees'"

    if " where " in user_input:
        parts = user_input.split(" where ")
        if len(parts) != 2:
            return "Error: only one where supported"

        condition_part = parts[1].strip()
        tokens = condition_part.split()

        if len(tokens) != 3:
            return "Error: use format column is value"

        column, operator, value = tokens

        if column not in valid_columns:
            return f"Error: column '{column}' not found"

        if operator not in ["is", "=", ">", "<"]:
            return "Error: use 'is', '=', '>', or '<'"

        # simple numeric vs text
        if value.isdigit():
            sql_value = value
        else:
            sql_value = f"'{value}'"

        sql_op = "=" if operator == "is" else operator
        return f"SELECT * FROM employees WHERE {column} {sql_op} {sql_value};"

    if user_input == "show employees":
        return "SELECT * FROM employees;"

    return "Error: invalid command"

def main():
    print("NLP to SQL Converter")
    print("Examples: show employees | show employees where department is sales")

    while True:
        try:
            user_input = input(">> ")
        except EOFError:
            break

        if user_input.lower() == "exit":
            break

        sql_output = parse_nlp_to_sql(user_input)
        print(sql_output)

if __name__ == "__main__":
    main()