import os
import openpyxl

# Folder containing all the input Excel files and where the output Excel file will be generated
input_folder = r'D:\Akhilesh\FileReaderProject'

def extract_data_from_excel(excel_file):
    """Extracts data from specific cells in the 'Document Control' tab of an Excel file."""
    workbook = openpyxl.load_workbook(excel_file, data_only=True)
    doc_control_sheet = workbook['Document Control']
    
    data = {
        "StoryName": get_named_cell_value(workbook, 'StoryName', doc_control_sheet),
        "GWID": get_named_cell_value(workbook, 'GWID', doc_control_sheet),
        "Description": get_named_cell_value(workbook, 'Description', doc_control_sheet),
        "StoryPoints": get_named_cell_value(workbook, 'StoryPoints', doc_control_sheet),
        "StoryAssumptions": get_named_cell_value(workbook, 'StoryAssumptions', doc_control_sheet)
    }
    
    workbook.close()
    return data

def get_named_cell_value(workbook, range_name, sheet):
    """Gets the value of a named cell range in a worksheet, or returns 'Not found' if not found."""
    for name in workbook.defined_names.definedName:
        if name.name == range_name:
            cells = list(name.destinations)
            if cells:
                cell = cells[0]
                value = sheet[cell[1]].value
                return value
    return 'Not found'

def write_output_to_excel(output_file, data_list):
    """Writes extracted data to the 'Output' tab of the specified Excel file."""
    workbook = openpyxl.Workbook()
    output_sheet = workbook.active
    output_sheet.title = 'Output'
    
    # Write header row
    header = ["Name of the source excel", "StoryName", "GWID", "Description", "StoryPoints", "StoryAssumptions"]
    output_sheet.append(header)
    
    # Write data rows
    for data in data_list:
        row_data = [
            data['SourceExcel'],
            data['StoryName'],
            data['GWID'],
            data['Description'],
            data['StoryPoints'],
            data['StoryAssumptions']
        ]
        output_sheet.append(row_data)
    
    # Save the workbook to the output file
    workbook.save(output_file)

if __name__ == "__main__":
    data_list = []
    
    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.xlsx'):
            excel_file_path = os.path.join(input_folder, filename)
            # Extract data from the Excel file
            data = extract_data_from_excel(excel_file_path)
            # Store extracted data along with source Excel name
            data['SourceExcel'] = filename[:-5]  # Remove '.xlsx' extension from filename
            data_list.append(data)
    
    # Define the path for the output Excel file
    output_file = os.path.join(input_folder, 'Output.xlsx')
    
    # Write extracted data to Output.xlsx in the input folder
    write_output_to_excel(output_file, data_list)
    
    print(f"Data extraction and writing to {output_file} complete.")
