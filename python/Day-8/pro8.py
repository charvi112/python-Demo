def sum_numbers_in_file(file_path):
    total_sum = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
            
                number = int(line.strip())
                total_sum += number

        print(f"The sum of all numbers in the file is {total_sum}.")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except ValueError:
        print("The file contains non-numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'C:\python\Day-8\number.csv' 
sum_numbers_in_file(file_path)
