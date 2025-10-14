import pandas as pd

def extract_and_print_headers(excel_path):
    """Extract and print column headers from Excel sheet"""
    df = pd.read_excel(excel_path)
    headers = df.columns.tolist()
    
    print("Column Headers:")
    for i, header in enumerate(headers, 1):
        print(f"{i}. {header}")
    
    return headers

# Usage
if __name__ == "__main__":
    excel_file = r"C:\Users\HariVardhanaShubhash\Downloads\OneDrive_2025-10-09 1\Ops Bot\Account Details\Platform, App & Infra.xlsx"
    headers = extract_and_print_headers(excel_file)