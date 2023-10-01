# dictionaries(changeable,unordered collection of unique key,pair fast because they are hashing, allow us to access a value quickly)
# (key:value)

capitals = {'USA':'washington',
            'India':'New dehli'
            ,'chine':'Beiing',
            'Russia':'Moscow'}

print(capitals['Russia'])

print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Geramny':'Berlin'})
capitals.update({ 'USA':'Las Vegas'})
capitals.pop('Russia')
capitals.clear()

for key,value in capitals.items():
    print(key,value)


# index operator[]
# (give access to a sequence element(str,list,tuples))
name="maham jamil"
if(name[0].islower()):
    name=name.capitalize()

first_name=name[0:3].upper()
last_name=name[4:].upper()
print(name)
print(first_name)
print(last_name)

last_character=name[-1]
print(last_character)


# function(executed when called)
def hello(name,last_name,age):
    print("Hello "+name+last_name)
    print("you are " + str(age)+ " years old" )
# my_name="maham"
# hello(argument)
# hello("Maham","jamil")
# hello(my_name)
hello("maham ","jamil",22)

# return statement

def multiply(num1,num2):
    result=num1+num2
    return result
x=multiply(6,8)
print(x)

# keyword arguments()
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)
hello(last="jamil",middle="maham",first="MJS")

# nested function calls

# print(round(abs(float(input("Enter a whole positive number :")))))


# variable scope(A var is available from inside the region it is created)

# global var(available inside and outside)
name="maham"
# local variable(it has only scope from inside)
def display_name():
    name="maham jamil"
    print(name)

display_name()
print(name)

# *args(pack all argu into tuple
# function can accept varying amount of arguments)

def add(*args):
    sum=0
    args=list(args)
    args[1]=0
    for i in args:
        sum=sum+i
    return sum

print(add(1,3,4,5,6))


# **kwargs(pack all argu into dictionary
# and useful so that function can accept varing amount of keyword arguments)


def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


hello(title="coder",first="maham",middle="jamil",last="MJ")






















































