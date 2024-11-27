# Define the lists
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
scores = [88, 42, 79, 95, 33]
# Sort students by score
sorted_students_scores = sorted(zip(students, scores), key=lambda x: x[1], reverse=True)
sorted_students = [student for student, score in sorted_students_scores]
sorted_scores = [score for student, score in sorted_students_scores]
print("Sorted list of students by score:")
for student, score in sorted_students_scores:
 print(f"{student}: {score}")
# Find the highest and lowest scores
highest_score = max(scores)
lowest_score = min(scores)
highest_scorers = [students[i] for i in range(len(scores)) if scores[i] == highest_score]
lowest_scorers = [students[i] for i in range(len(scores)) if scores[i] == lowest_score]
print(f"The highest score is: {highest_score} ({', '.join(highest_scorers)})")
print(f"The lowest score is: {lowest_score} ({', '.join(lowest_scorers)})")
# Calculate the average score
average_score = sum(scores) / len(scores)
print(f"The average score is: {average_score:.2f}")
# Determine the number of students who passed
passing_threshold = 50
passed_students = [students[i] for i in range(len(scores)) if scores[i] > passing_threshold]
number_of_passed_students = len(passed_students)
print(f"The number of students who passed is: {number_of_passed_students}")
print(f"Students who passed: {', '.join(passed_students)}")