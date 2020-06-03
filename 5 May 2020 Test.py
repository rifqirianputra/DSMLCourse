print("hello world")
print ('hello world')
print ("""hello world""")

name = "Bob Windcaller"
age = 25
height = 179.5

print(type(height))
print(type(age))
print(type(name))

print("name:", name)
print("age", age)
print ("height", height)

print("name:", name, "age:", age, "height:", height)
print("name: {}, age: {}, height: {}" .format(name,age,height))
print("name: %s, age: %d, height: %f" %(name, age, height))
print(f"name: {name}, age: {age}, height: {height}")


print(name)
print(len(name))
print(name.lower())
print(name.upper())

print(name.replace("Bob","Jurgen"))
print(name.lower())

print(name[5])

print(name[0:3:1])
print(name[0:3])
print(name[:3])
print(name[4:14])
print(name.index('l'))

print(name.split(" "))