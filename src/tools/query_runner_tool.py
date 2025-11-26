import pandas as pd
from pandasql import sqldf
from google.adk.tools import FunctionTool

def create_sql_tool(df: pd.DataFrame):
    """Create a SQL tool with the provided DataFrame"""
    def run_sql_query(sql: str) -> str:
        try:
            # Print the SQL generated to the terminal
            print(f"\n=== SQL Query Executed ===")
            print(f"SQL: {sql}")
            print(f"DataFrame shape: {df.shape}")
            print(f"DataFrame columns: {list(df.columns)}")
            print("=" * 30)
            
            result = sqldf(sql, {"df": df})
            if result is None or result.empty:
                return "NO_DATA_FOUND"
            return result.to_string(index=False)
        except Exception as e:
            print(f"SQL Error: {e}")
            return f"SQL_ERROR: {e}"
    
    return FunctionTool(func=run_sql_query)