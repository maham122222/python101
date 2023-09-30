#loop control statements
# break = terminate loop entirely
# continue = skips to the next iteration of the code


# while True:
#     name=input("Enter your name ? :")
#     if name!="":
#         break

phone_number="123-45-6565"

for i in phone_number:
    if i=="-":
        continue
    print(i, end="")


for i in range(1,21):
    if i ==13:
        pass
    else:
        print(i)



# list(a variable that can store multiple items)
food = [ "pizza","burger","hotdog","pudding"]
food[0]="sushi"
print(food[2])
print(food[0])
food.append("icecream")
food.append("momos")
food.remove("hotdog")
food.insert(0,"cake")
food.sort()

# pop will remove the last element
food.pop()
# food.clear()

for i in food:
    print(i,end=",")


# 2D list=a list of list

drinks=['coffe',"soda","tea"]
dinner=["pizza","burger","hotdog"]
desert=["cake",'ice cream']


food=[drinks,dinner,desert]
print(food)
print(food[0])
print(food[0][0])

# tuple (ordered and unchangeable , used to group together
# related data)

student = ("maham",22,"female")
print(student.count("maham"))
print(student.index("female"))

for i in student:
    print(i)

if "maham" in student:
    print("maham is here")


# set(unordered,unindexed, when u run the next time the order of values will be change)
# no duplicate values

utensils={"fork","spoon","knifes"}
utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()

dishes={"bowl","plate","cup","knifes"}
# to add dishes set to utensils set
# utensils.update(dishes)
# dinner_table=utensils.union(dishes)

# for i in utensils:
    # print(i , end=",")

# for i in dinner_table:
    # print(i)


# what utensils have that dishes does'nt
# print(utensils.difference(dishes))


# return comman thing
print(utensils.intersection(dishes))





























