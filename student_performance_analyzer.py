import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
data = pd.read_csv('student_marks.csv')

# Step 2: Calculate average marks for each student
data['Average'] = data[['Math', 'Science', 'English']].mean(axis=1)

# Step 3: Determine pass or fail (average >= 60)
data['Result'] = data['Average'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

# Step 4: Calculate subject-wise averages
subject_avg = data[['Math', 'Science', 'English']].mean()

# Step 5: Find top 3 students
top_students = data.sort_values(by='Average', ascending=False).head(3)

# Step 6: Print results
print("=== Student Performance Summary ===\n")
print(data)
print("\nSubject-wise Average Marks:")
print(subject_avg)
print("\nTop 3 Students:")
print(top_students[['Name', 'Average']])

# Step 7: Optional - Visualization
plt.bar(data['Name'], data['Average'])
plt.title('Average Marks of Students')
plt.xlabel('Student')
plt.ylabel('Average Marks')
plt.show()
