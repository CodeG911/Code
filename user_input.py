import csv

# Function to collect user input
def collect_data():
    sales_data = []
    while True:
        sales = input("Enter sales amount (or type 'done' to finish): ")
        if sales.lower() == 'done':
            break
        month = input("Enter month: ")
        category = input("Enter category: ")
        
        # Append collected data to the list
        sales_data.append([sales, month, category])
    
    return sales_data

# Function to save data to a CSV file
def save_to_csv(data, filename='sales_data.csv'):
    # Specify the column headers
    headers = ['Sales', 'Month', 'Category']
    
    # Writing to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers to the first row
        writer.writerows(data)   # Write the actual data
        
    print(f"Data saved to {filename}")

# Main script
data = collect_data()  # Collect data from user
save_to_csv(data)      # Save the data to CSV file
