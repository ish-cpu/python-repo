import random
# # A list that will contain student names
# student_name = ["kate Spade", "Alexander McQueen", "Vera Wang", "Ted Blake", "Giorgio Armani"]

# #A list that will contain student id numbers
# student_id = []

# #import random lib to generate random int.
# import random

# #An empty list to store student emails
# student_email = []

# #use student name so further additions will be updated
# #remeber () executes first
# for i in range(len(student_name)):
#     [first, last] = student_name[i].split(" ")
#     student_id.append(random.randint(111111, 999999))
#     student_email.append(first[0] + last + str(student_id[i])[-3:] + "@example.com")
#     print(f"name: {student_name[i]}\n id: {student_id[i]}\n email: {student_email[i]}")
#     print("")

#import random
import random 

student_data = []
#initialize dictionary to store student information
 #name, ID, email 

#use single loop to populate dictionaries
#student_name = ["kate Spade", "Alexander McQueen", "Vera Wang", "Ted Blake", "Giorgio Armani"]
student_name = ["kate Spade", "Alexander McQueen", "Vera Wang", "Ted Blake", "Giorgio Armani"]
for i in range(len(student_name)):
    student = {}
    student["name"] = student_name[i]
    [first, last] = student_name[i].split(" ")
    student["ID"] = random.randint(111111,999999)
    student["email"] = first[0] + last + str(student["ID"])[-3:] + "@example.com"
    
    student_data.append(student)

#using a separate for loop ensures the print statement is not hardcoded
for data in student_data:
    print("")
    for key in student:
        print(f"{key}: {student[key]}")
#     print(f"name: {data["name"]}\nId: {data["ID"]}\nemail: {data["email"]}")
#     print("")
