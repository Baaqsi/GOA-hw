""""
#1
list = []
for x in range(1,11):
    list.append(x)
print(len(list))
"""

"""
usr1 = int(input("enter first number: "))
usr2 = int(input("enter second number: "))

list = []
for x in range(usr1,usr2):
    list.append(x)

print(list)

"""


"""
#3
user1 = int(input("enter the first number:  "))
user2 = int(input("enter the second number: "))

list = []
for x in range(user1,user2):
    list.append(x)


print(min(list))
print(max(list))
print(sum(list))    
"""

"""
#4
rows = int(input("please enter rows: "))

numbers = []
for x in range(1,rows + 1):
    ask = int(input(f"(asked = {x})please enter your desired number: "))
    numbers.append(ask)

print(sum(numbers))

"""

"""
#5
names = ["luka","gio","givi","lazare","nika"]
list1 = names[:3]
print(list1)
list2 = names[3:]
print(list2)        
list3 = names[-3:-1]
print(list3)
"""


"""
names = ["luka","gio","givi","lazare","luka","nika"]

for name in names:
    if name == "luka":
        print("hello admin")
    else:
        print("hello user")
"""