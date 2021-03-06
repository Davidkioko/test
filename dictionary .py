#DICTIONARY
print("Hello world")
student = {
    "fname" : "Diego",
    "lname" : "santos",
    "phone" : "0722000000",
    "email" : "diegosantos13802@gmail.com"
}
print(student)

car= {
    "brand" : "Ford",
    "electric" : False,
    "year" : 2015,
    "colors" : ["red", "white", "blue"],
    "model" : "Mustang"
}
print(car)

#Accesing Items you can access the item of dictionary by referring to its key name,iside square brackets
#car = {
   # "brand" : "Ford",
   ## "model" : "Mustang",
#"year"  : 1964
#}
x = car ["model"]
print(x)

x = student ["fname"]
print(x)

#get the value of the "model" key
x= car.get("brand")
print(x)

x=student.get("email")
print(x)

#check if key exists

if "model" in car:
    print("Yes, 'model' is one of the keys in this dictionary")
if "email" in student:
    print("Yes, 'email' is one of the keys in this dictionary")
    
#change dictionary items

car ["year"] = 2018
print(car)
student ["lname"] = "Ray"
print(student)

#Add dictionary items

car ["color"] = "red"
print(car)

#Removing Items

car.pop("model")
print(car)

#loop through a dictionary
for x in car :
    print(x)
for x in car.values():
    print(x)

for x in car.keys():
    print(x)
for x,y in car.items():
   print(x,y)
   
#Nested Dictionary

myfamily = {
    "child1" : {
        "name" : "Emily",
        "year" : 2004
        },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
        },
        "child3" : {
        "name" : "linus",
        "year" : 2011
        },
    }
print(myfamily)

#copy dictionaries
 
car = car.copy()
print(car)


    






