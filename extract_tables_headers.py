import pandas as pd

def extract_tables_and_headers(excel_path):
    """Extract all tables and their headers from Excel sheet"""
    # Read all sheets
    excel_file = pd.ExcelFile(excel_path)
    
    for sheet_name in excel_file.sheet_names:
        print(f"\n=== Sheet: {sheet_name} ===")
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        
        print(f"Headers ({len(df.columns)} columns):")
        for i, header in enumerate(df.columns, 1):
            print(f"  {i}. {header}")
        
        print(f"Rows: {len(df)}")
        print(f"Sample data (first 3 rows):")
        print(df.head(3).to_string())

# Usage
if __name__ == "__main__":
    excel_file = r"C:\Users\HariVardhanaShubhash\Downloads\OneDrive_2025-10-09 1\Ops Bot\Account Details\Platform, App & Infra.xlsx"
    extract_tables_and_headers(excel_file)