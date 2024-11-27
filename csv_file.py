import csv

# Read data from CSV file
def read_csv(filename):
    with open(filename, 'r') as file:
        return [{'name': row['name'], 'age': int(row['age']), 'grade': row['grade']}
                for row in csv.DictReader(file)]

# Main function
def main():
    filename = 'students_info.csv'
    try:
        students = read_csv(filename)
        
        if not students:  # Handle case where no data is present
            print("No student data found.")
            return
        
        # Data processing
        total_students = len(students)
        average_age = sum(student['age'] for student in students) / total_students
        oldest = max(students, key=lambda x: x['age'])
        youngest = min(students, key=lambda x: x['age'])

        # Results
        print(f"Total students: {total_students}")
        print(f"Average age: {average_age:.2f}")
        print(f"Oldest: {oldest['name']} (Age: {oldest['age']})")
        print(f"Youngest: {youngest['name']} (Age: {youngest['age']})")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError as e:
        print(f"Error in data formatting: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
