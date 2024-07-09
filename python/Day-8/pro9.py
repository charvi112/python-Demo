import json

def employee(file_path):
    try:
    
        with open(file_path, 'r') as file:
            data = json.load(file)
        
    
        employee_info = []
        for employee in data.get('employees', []):
            name = employee.get('name')
            department = employee.get('department')
            employee_info.append({'name': name, 'department': department})
        
        return employee_info

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

file_path = 'C:\python\Day-8\data.json'
employee_info = employee(file_path)
print(employee_info)
