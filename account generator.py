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

student_data = []
#initialize dictionary to store student information
 #name, ID, email 
student = {}  
#use single loop to populate dictionaries
#student_name = ["kate Spade", "Alexander McQueen", "Vera Wang", "Ted Blake", "Giorgio Armani"]
student_name = ["kate Spade", "Alexander McQueen", "Vera Wang", "Ted Blake", "Giorgio Armani"]
for i in range(len(student_name)):
    student["name"] = student_name[i]
    student["ID"] = random.randint(111111,999999)
    student["email"] = student["name"] + str(student["ID"]) + "@example.com"
    #print(student)
    student_data.append(dict(student))
    print(student_data[i])