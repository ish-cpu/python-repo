# A list that will contain student names
student_name = ["kate Spade", "Alexander McQueen", "Vera Wang", "Ted Blake", "Giorgio Armani"]

#A list that will contain student id numbers
student_id = []

#import random lib to generate random int.
import random

#An empty list to store student emails
student_email = []

#use known range to generate name, email and id
for i in range(5):
    [first, last] = student_name[i].split(" ")
    student_id.append(random.randint(111111, 999999))
    student_email.append(first[0] + last + str(student_id[i]) + "@example.com")
    print(f"name: {student_name[i]}\n id: {student_id[i]}\n email: {student_email[i]}")
    print("")