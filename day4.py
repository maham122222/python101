# str.format() = optional method that gives user more control when displaying output

animal="cow"
item="moon"

# print("The"+animal+"jumped over the"+item)
# print("The {} jumped over the {}".format("cow","moon"))
# print("The {} jumped over the {}".format(animal,item))

# positional argument
# print("The {0} jumped over the {1}".format(animal,item))


# keyword argument
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))


text="The {} jumped over the {}"
print(text.format(animal,item))


name="maham"

# to add padding
print("hello, my name is {}".format(name))
print("hello, my name is {:10}".format(name))
print("hello, my name is {:>10}".format(name))
print("hello, my name is {:<10}".format(name))
print("hello, my name is {:^10}".format(name))
# print("hello, my name is {name:10}. Nice to meet you".format(name))

number=1000
# f is for floating point number
print("The number pi is {:.4f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:x}".format(number))
print("The number is {:E}".format(number))

# random module
import random

x = random.randint(1,6)
y=random.random() #generate from 0 -1

my_list=['rock','paper','scissors']
z=random.choice(my_list)
print(x)
print(y)
print(z)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']

random.shuffle(cards)
print(cards)

# exception (events dectected during execution that interrupt the flow of program)

try:
    numerator = int(input("Enter a number to divide :"))
    denominator = int(input("Enter a number to divide :"))
    result=numerator/denominator
    
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero : ")
except ValueError as e:
    print(e)
    print("Enter only number please")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")




















































