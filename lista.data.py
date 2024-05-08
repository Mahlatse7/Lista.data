import csv

# Data to be written to the CSV file
data = [
    {'Name': 'Agnes', 'Age': 30, 'City': 'Cape Town'},
    {'Name': 'Precious', 'Age': 25, 'City': 'Pretoria'},
    {'Name': 'John', 'Age': 20, 'City': 'Johannesburg'}
]

# Specify the file name
file_name = 'data.csv'

# Writing to CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    
    # Write header
    writer.writeheader()
    
    # Write data
    for row in data:
        writer.writerow(row)

print(f"CSV file '{file_name}' has been generated.")
