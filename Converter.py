def parse_nlp_to_sql(user_input):
    user_input = " ".join(user_input.lower().split())

    valid_columns = ["id", "name", "department", "salary", "hire_date", "city", "age"]

    if not user_input.startswith("show employees"):
        return "Error: command should start with 'show employees'"

    order_query = ""
    if " order by " in user_input:
        user_input, order_part = user_input.split(" order by ")
        tokens = order_part.split()
        column = tokens[0]
        if column not in valid_columns:
            return f"Error: column '{column}' not found"
        direction = tokens[1].upper() if len(tokens) > 1 and tokens[1] in ["asc", "desc"] else "ASC"
        order_query = f" ORDER BY {column} {direction}"

    sql_base = "SELECT * FROM employees"
    where_clause = ""

    if " where " in user_input:
        parts = user_input.split(" where ")
        if len(parts) != 2:
            return "Error: only one where supported"

        conditions = parts[1].strip().split(" and ")
        sql_conditions = []

        for cond in conditions:
            tokens = cond.strip().split()
            if len(tokens) != 3:
                return "Error: use format column is value"

            column, operator, value = tokens
            if column not in valid_columns:
                return f"Error: column '{column}' not found"

            if operator not in ["is", "=", ">", "<"]:
                return "Error: use 'is', '=', '>', or '<'"

            sql_value = value if value.isdigit() else f"'{value}'"
            sql_op = "=" if operator == "is" else operator
            sql_conditions.append(f"{column} {sql_op} {sql_value}")

        where_clause = f" WHERE {' AND '.join(sql_conditions)}"
    elif user_input != "show employees":
        return "Error: invalid command"

    return f"{sql_base}{where_clause}{order_query};"

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