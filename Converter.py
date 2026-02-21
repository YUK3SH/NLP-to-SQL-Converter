def parse_nlp_to_sql(user_input):
    user_input = " ".join(user_input.lower().replace(",", " ").split())
    valid_columns = ["id", "name", "department", "salary", "hire_date", "city", "age"]

    if not (user_input.startswith("show") or user_input.startswith("count")):
        return "Error: command should start with 'show' or 'count'"

    order_query = ""
    if " order by " in user_input:
        user_input, order_part = user_input.split(" order by ")
        tokens = order_part.split()
        if tokens[0] not in valid_columns: return f"Error: column '{tokens[0]}' not found"
        dir = tokens[1].upper() if len(tokens) > 1 and tokens[1] in ["asc", "desc"] else "ASC"
        order_query = f" ORDER BY {tokens[0]} {dir}"

    sql_base = "SELECT * FROM employees"
    if user_input.startswith("count employees"):
        sql_base = "SELECT COUNT(*) FROM employees"
        user_input = user_input.replace("count employees", "show employees", 1)

    if user_input.startswith("show "):
        parts = user_input.split(" where ")
        head = parts[0].replace("show ", "", 1).strip()
        if head != "employees":
            cols = [c.strip() for c in head.replace(" and ", " ").split() if c.strip()]
            for c in cols:
                if c not in valid_columns: return f"Error: column '{c}' not found"
            if sql_base.startswith("SELECT *"): sql_base = f"SELECT {', '.join(cols)} FROM employees"

    where_clause = ""
    if " where " in user_input:
        parts = user_input.split(" where ")
        if len(parts) != 2: return "Error: only one where supported"
        
        where_text = parts[1].strip().replace("is not ", "not ")
        tokens = where_text.split()
        conditions, idx = [], 0
        while idx < len(tokens):
            if idx + 1 < len(tokens) and tokens[idx+1] == "between":
                conditions.append((" ".join(tokens[idx:idx+5]), ""))
                idx += 5
            else:
                conditions.append((" ".join(tokens[idx:idx+3]), ""))
                idx += 3
            if idx < len(tokens) and tokens[idx] in ["and", "or"]:
                conditions[-1] = (conditions[-1][0], tokens[idx].upper())
                idx += 1

        sql_conds = []
        for cond, sep in conditions:
            ts = cond.split()
            if "between" in ts:
                if len(ts) != 5: return "Error: invalid between format"
                col, _, v1, _, v2 = ts
                if col not in valid_columns: return f"Error: column '{col}' not found"
                v1, v2 = [v if v.isdigit() else f"'{v}'" for v in [v1, v2]]
                sql_conds.append(f"{col} BETWEEN {v1} AND {v2}")
            else:
                if len(ts) != 3: return "Error: use format column is value"
                col, op, val = ts
                if col not in valid_columns: return f"Error: column '{col}' not found"
                if op == "not": op = "!="
                if op not in ["is", "=", ">", "<", ">=", "<=", "!="]: return "Error: use valid operator"
                sql_val = val if val.isdigit() else f"'{val}'"
                sql_op = "=" if op == "is" else op
                sql_conds.append(f"{col} {sql_op} {sql_val}")
            if sep: sql_conds.append(sep)

        where_clause = f" WHERE {' '.join(sql_conds)}"

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