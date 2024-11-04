#Array
from First_Python_Project.strings import course

courses = ["MIT","Cybersecurity","Datascience"]
print(courses)

#Accessing an element in array
print(courses[1])

#looping through an element
for y in courses:
    print("Course is :",y)


# Adding a new element into an array
courses.append("Web Development")
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)

#Adding another element
courses.insert(2,"Graphic Design")
for m in courses:
 print("New courses is:",m)