import pdfplumber
import pandas as pd
import json

def extract_tables_from_pdf(pdf_path):
    """
    Extract all table data from a PDF file using pdfplumber
    """
    all_tables = []
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"PDF has {len(pdf.pages)} pages")
        
        for page_num, page in enumerate(pdf.pages):
            print(f"\nProcessing page {page_num + 1}...")
            
            # Extract tables from the page
            tables = page.extract_tables()
            
            if tables:
                print(f"Found {len(tables)} table(s) on page {page_num + 1}")
                
                for table_num, table in enumerate(tables):
                    print(f"  Table {table_num + 1}: {len(table)} rows, {len(table[0]) if table else 0} columns")
                    
                    # Store table with metadata
                    table_data = {
                        'page': page_num + 1,
                        'table_number': table_num + 1,
                        'data': table
                    }
                    all_tables.append(table_data)
                    
                    # Print first few rows of each table for preview
                    print(f"  Preview of table {table_num + 1}:")
                    for i, row in enumerate(table[:5]):  # Show first 5 rows
                        print(f"    Row {i + 1}: {row}")
                    if len(table) > 5:
                        print(f"    ... and {len(table) - 5} more rows")
            else:
                print(f"No tables found on page {page_num + 1}")
    
    return all_tables

def save_tables_to_csv(tables, base_filename="extracted_table"):
    """
    Save extracted tables to CSV files
    """
    for i, table_info in enumerate(tables):
        if table_info['data']:
            # Create DataFrame from table data
            df = pd.DataFrame(table_info['data'])
            
            # Use first row as headers if it looks like headers
            if len(df) > 1:
                # Check if first row contains mostly strings (likely headers)
                first_row_strings = sum(1 for cell in df.iloc[0] if isinstance(cell, str) and cell and not cell.isdigit())
                if first_row_strings > len(df.columns) / 2:
                    df.columns = df.iloc[0]
                    df = df.drop(df.index[0]).reset_index(drop=True)
            
            # Save to CSV
            filename = f"{base_filename}_page{table_info['page']}_table{table_info['table_number']}.csv"
            df.to_csv(filename, index=False)
            print(f"Saved table to {filename}")

def main():
    pdf_path = "data/Agprice_table.pdf"
    
    print(f"Extracting tables from: {pdf_path}")
    print("=" * 50)
    
    try:
        # Extract all tables
        tables = extract_tables_from_pdf(pdf_path)
        
        print(f"\n" + "=" * 50)
        print(f"SUMMARY: Found {len(tables)} table(s) total")
        
        if tables:
            # Save tables to CSV files
            print("\nSaving tables to CSV files...")
            save_tables_to_csv(tables, "agprice_table")
            
            # Also save raw table data as JSON for reference
            with open("agprice_tables_raw.json", "w") as f:
                json.dump(tables, f, indent=2)
            print("Saved raw table data to agprice_tables_raw.json")
            
        else:
            print("No tables were found in the PDF")
            
    except Exception as e:
        print(f"Error processing PDF: {e}")

if __name__ == "__main__":
    main()
