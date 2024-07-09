import csv

def calculate_average_salary(csv_file):
    total_salary = 0
    employee_count = 0

    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                total_salary += float(row['Salary'])
                employee_count += 1

        if employee_count == 0:
            print("No employee data found in the file.")
        else:
            average_salary = total_salary / employee_count
            print(f"The average salary of all employees is {average_salary:.2f}")

    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
csv_file = 'C:\python\Day-8\employee.csv' 
calculate_average_salary(csv_file)
