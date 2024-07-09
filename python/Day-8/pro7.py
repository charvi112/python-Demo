import csv

def calculate_total_sales(csv_file, target_product):
    total_revenue = 0

    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row['Product'] == target_product:
                    quantity = int(row['Quantity'])
                    price = float(row['Price'])
                    total_revenue += quantity * price

        print(f"The total sales revenue for {target_product} is {total_revenue:.2f}")

    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


csv_file = 'C:\python\Day-8\sales.csv'  
target_product = 'Laptop'  
calculate_total_sales(csv_file, target_product)
