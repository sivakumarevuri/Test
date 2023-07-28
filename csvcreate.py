import csv
import random
import os

current_dir = '/home/lucifer/Desktop/siva/data/'
branch = ['CSE', 'ECE', 'IT', 'EEE', 'CIVIL']
fields = ["Student_id", "Branch", "Percentage"]
file_path = os.path.join(current_dir, 'student_data.csv')
# filename = "/home/lucifer/Desktop/siva/data/student_data.csv"
length = len(pd.read_csv(file_path))

# print(length)

with open(file_path, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)

    # csvwriter.writerow(fields)

    for i in range(length + 1, length + 6):
        temp = []
        x = str(('%04d' % i))
        temp.append(x)
        x = random.randint(0, 4)
        temp.append(branch[x])
        x = random.randint(50, 99)
        temp.append(x)
        csvwriter.writerow(temp)
print("The data is created successfully")
