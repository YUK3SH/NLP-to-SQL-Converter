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
        if len(parts) != 2: return "Error: only one where supported"

        # Token-based parsing to handle BETWEEN and AND correctly
        where_text = parts[1].strip().replace("is not ", "not ")
        where_tokens = where_text.split()
        conditions, idx = [], 0
        while idx < len(where_tokens):
            if idx + 1 < len(where_tokens) and where_tokens[idx+1] == "between":
                conditions.append(" ".join(where_tokens[idx:idx+5]))
                idx += 5
            else:
                conditions.append(" ".join(where_tokens[idx:idx+3]))
                idx += 3
            if idx < len(where_tokens) and where_tokens[idx] == "and": idx += 1

        sql_conditions = []
        for cond in conditions:
            if "between" in cond:
                tokens = cond.split()
                if len(tokens) != 5: return "Error: invalid between format"
                col, _, v1, _, v2 = tokens
                if col not in valid_columns: return f"Error: column '{col}' not found"
                v1,v2 = [v if v.isdigit() else f"'{v}'" for v in [v1, v2]]
                sql_conditions.append(f"{col} BETWEEN {v1} AND {v2}")
            else:
                cond = cond.replace("is not", "!=")
                tokens = cond.split()
                if len(tokens) != 3: return "Error: use format column is value"
                col, op, val = tokens
                if op == "not": op = "!="
                if col not in valid_columns: return f"Error: column '{col}' not found"
                if op not in ["is", "=", ">", "<", ">=", "<=", "!="]:
                    return "Error: use 'is', '=', '>', '<', '>=', '<=', or '!='"
                sql_val = val if val.isdigit() else f"'{val}'"
                sql_op = "=" if op == "is" else op
                sql_conditions.append(f"{col} {sql_op} {sql_val}")

        where_clause = f" WHERE {' AND '.join(sql_conditions)}"
    elif user_input != "show employees":
        return "Error: invalid command"

    return f"{sql_base}{where_clause}{order_query};"

def main():
    print("----------------------")
    print("NLP to SQL Converter")
    print("----------------------")

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