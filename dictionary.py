a={
    "no":32,
    "name":"john",
    "class":"cse-a"
    }
print(a["name"])
print(a.get("no"))

#another method to define dict

a=dict(name="steve",rollno=32,dept="it")
print(a)

#add a key
a["email"]="aaa@gmail.com"
a["phno"]=342323422
a["phno"]=676876128
print(a)

#delete a key
del a["email"]
print(a)
print(a.pop("phno"))

print(a.keys())
print(a.values())
print(a.items())
print(a.pop("name"))
print(a.update({"name":"kumar"}))

student={
    "name":"shan",
    "mark":89,
    "age":23
    }
for i in student:
   print(i,":",student[i]) 
student["email"]="shan@gmail.com"
print(student)
student["name"]="shann"
print(student)
print(student.values())
del student["name"]
print(student)

