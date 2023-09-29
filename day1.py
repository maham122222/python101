import math
import time

#variables
first_name = "maham"
last_name="jamil"
full_name= first_name+last_name
print("hello" + full_name)

# int(cannot store decimal number)
age =22
age = age +1
# if you want to use string with another data type convert it into string like we have converted age into string
print("Your age is "+str(age))
print(type(age))


# float(stores decimal number)
height=250.56
print(height)
print("Your height is " + str(height) +"cm")
print(type(height))


# boolean(true or false)
human =False
print(human)
print("are you a human"+str(human))
print(type(human))


# multiple asiignment
name,age,attractive="maham","22",True

sam=sara=maham=30


# string methods:
# length method
name="maham"
print(len(name))
print(name.find("h"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('a'))
print(name.replace('a','o'))
print(name*3)



# typecasting=convert the datatype of a value to another 
# datatype
x=1
y=2.2
z="5"
y=int(y)
z=int(z)
print(y)
print(z*5)

x=float(x)
print(x)

print("x is str", str(x))



# input
# name=input("what is your name ?")
# age=int(input("how old are you : "))
# height=float(input("What is your height : "))
# age=age+1
# print('Hello ' +name)
# print("you are" +str(age)+"years old")
# print("you are " +str(height)+"cm tall")


pi=3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(66))


x=1
y=2
z=3

print("Max num is" ,max(x,y,z))
print("Min num is",min(x,y,z))


# indexing [start:stop:step]


name="maham jamil"

first_name=name[0:5]
last_name=name[6:11]
print(first_name)
print(last_name)

third_name=name[0:8:2]
print(third_name)

reversed_name=name[::-1]

# slicing (start,stop,step)

website="https://google.com"
website1="hhtp://wikipedia.com"

slice=slice(8,-4)
print(website[slice])
print(website1[slice])

# if-else
# age=int(input("how old are you : ?"))
# if age>=18:
#     print("You are an adult")
# elif age == 100:
#     print("You are a century old")
# elif age<0:
#     print("You are not born")
# else:
#     print("You are a child")


# logical operators (and,or,not)
# temp=(int(input("What is the temprature outside? :")))

# if (temp >=0  and temp <=30):
#     print("the temprature is good today")
#     print("go outside")
# elif (temp<0 or temp>30):
#     print("The temprature is bad today")
    # print("stay inside")

# using not operator (works opposite)
# if not(temp >=0  and temp <=30):
#     print("the temprature is good today")
#     print("go outside")
# elif not(temp<0 or temp>30):
#     print("The temprature is bad today")
#     print("stay inside")

# while loop (execute code as it's condition remains true)

name=""
while len(name)==0: # /while not name:
    name=input("Enter your name")

print("hello" + name)


# for loops (execute code for a limited amount of time)
# while loop(unlimited)
# for loop(limited)

for i in range(10):
    print(i+1)

for i in range(10,20,2): #(inclusive,exclusive,step)
    print(i+1)

for i in ("maham jamil"):
    print (i)


# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)
# print("happy new year")



# nested loop

rows=int(input("how many rows ? :"))
columns=int(input("how many columns ? :"))

symbol = input("enter a symbol to use")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()














































 



















































