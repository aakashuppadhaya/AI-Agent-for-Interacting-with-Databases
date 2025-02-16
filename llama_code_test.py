from llama_cpp import Llama
from sqlalchemy import create_engine, text
import re

# Initialize Local LLM (CodeLlama Instruct)
llm = Llama(
    model_path="./codellama-7b-instruct.Q4_K_M.gguf",  # Replace with your CodeLlama model path
    n_ctx=2048,
    n_threads=8  # Use all M3 performance cores
)

# Connect to PostgreSQL
engine = create_engine('postgresql://username:password@localhost:5432/test') #test will be the database name

def natural_language_to_sql(query):
    prompt = f"""<s>[INST] Convert the following natural language question into PostgreSQL SQL.
    Database schema: employees(id, name, department, salary)
    Question: {query}
    Answer: [/INST]"""

    response = llm(prompt, max_tokens=200, temperature=0.5, stop=["[/INST]"])
    return response['choices'][0]['text'].strip()

def execute_query(sql):
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        return [dict(row) for row in result.mappings()]

def safe_query(user_input):
    try:
        raw_sql = natural_language_to_sql(user_input)

        if "DROP" in raw_sql.upper() or "DELETE" in raw_sql.upper() or "INSERT" in raw_sql.upper() or "UPDATE" in raw_sql.upper() or "ALTER" in raw_sql.upper():
            return "Blocked potentially dangerous operation."

        sql_match = re.search(r"SELECT.*?;", raw_sql, re.DOTALL | re.IGNORECASE)
        if sql_match:
            sql = sql_match.group()
            return execute_query(sql)
        else:
            return "Could not extract valid SQL."

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or 'exit'): ")
        if query.lower() == 'exit':
            break
        result = safe_query(query)
        print("\nResult:", result)