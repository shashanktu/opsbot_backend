from folder_agent import find_best_file
from excel_sql_agent import process_excel_query
from google import generativeai as genai
from helpers.config import api

def smart_excel_query(user_query):
    """Find the best file and process the query"""
    # Find the most relevant file
    file_path = find_best_file(user_query)
    
    if file_path:
        print(f"Selected file: {file_path}")
        # Process the query with the selected file
        result = process_excel_query(file_path, user_query, api)
        return result
    else:
        return "Could not find a relevant file for your query."

# Usage
if __name__ == "__main__":
    query = input()
    
    print(f"\nQuery: {query}")
    result = smart_excel_query(query)
    print(f"Result: {result}")