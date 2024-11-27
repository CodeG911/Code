# Step 1: Read data from the input file and store it in a dictionary
def read_data(filename):
    student_scores = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, score = line.strip().split(',')
                student_scores[name] = float(score)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return student_scores

# Step 2: Calculate the average exam score
def calculate_average(scores):
    total_score = sum(scores.values())
    num_students = len(scores)
    return total_score / num_students if num_students > 0 else 0

# Step 3: Write student names and scores to a new text file
def write_data(filename, student_scores, average_score):
    with open(filename, 'w') as file:
        file.write("Student Name,Score\n")
        for name, score in student_scores.items():
            file.write(f"{name},{score}\n")
        file.write(f"\nAverage Score: {average_score:.2f}\n")

# Main function to execute the steps
def main():
    input_filename = 'students_scores.txt'
    output_filename = 'students_scores_output.txt'
    
    # Read data from file
    student_scores = read_data(input_filename)
    
    # If no data is read, exit the function
    if not student_scores:
        print(f"No data found in {input_filename}. Exiting program.")
        return
    
    # Calculate average score
    average_score = calculate_average(student_scores)
 
    # Write data to new file
    write_data(output_filename, student_scores, average_score)
    
    print(f"\nData has been processed and saved to {output_filename}")
    print(f"\nAverage Score: {average_score:.2f}\n")

if __name__ == '__main__':
    main()
