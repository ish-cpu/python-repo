import random
student_name = []
for i in range(5):
    #allow user enter students names 
    name = input("enter for students first and last name: ")
    student_name.append(name)
    

#create empty list for id
#used random sample instead of randint to generate unique ids
#random sample creates a list
#collected list and assigned to y variable 

student_id = []
y = random.sample(range(111111,999999), 5)
for n in y:
    student_id.append(n)

#create empty list for id
student_email = []     
for i in range(5):
    [first, last] = student_name[i].split(" ")
    student_email.append(first[0] + last + str(student_id[i])[-3:] + "@example.com")
    
for i in range(5):
    print(f"name: {student_name[i]}\n id: {student_id[i]}\n email: {student_email[i]}")

    print(" ")