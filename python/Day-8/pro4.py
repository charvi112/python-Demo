import csv

def find_student_with_highest_score(csv_file):
    highest_score = -1
    student_name = ""

    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                score = int(row['Score'])
                if score > highest_score:
                    highest_score = score
                    student_name = row['Name']

        if student_name:
            print(f"The student with the highest score is '{student_name}' with a score of {highest_score}.")
        else:
            print("No student data found in the file.")
    
    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


csv_file = r'C:\python\Day-8\student.csv' 
find_student_with_highest_score(csv_file)
