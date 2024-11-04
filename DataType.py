number=67 #integer
second=45.98 #float
name ="Bramuel" #string
isPythonInteresting = True #Bolean
print(number,second,name,isPythonInteresting)

#Data Structures -Multiple values stored in a single Varialbe
cars = ["Toyota","Nissan","vw"] #List - Ordered and Changeable
fruits = ("Banana","apple","mango") #Tuple -Ordered but Unchangeable
countries= {"Kenya","Tunisia","Algeria"} #Set - Unordered and Unchangeable
student={
    "firstname":"Jane",
    "Age": 25,
    "Course":"Web Development",
    "gender" : "Female"
} #Dictionary - Key-value pair

print(cars)
print(fruits)
print(countries)
print(student ["gender"])

#Dertermining a DataType
print(type(countries))
print(type(student))

#Typecasting - its simply changing one datatype  to another
print(float(number))
print(int(second))

