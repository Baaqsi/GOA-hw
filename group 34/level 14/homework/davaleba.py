#while loops
#1
#import time

#dro = int(input("enter your desired number: "))

#while dro >= 1:
#    dro -= 1
#    print(dro)
#    time.sleep(1)
#    if dro == 1:
#        print("times up nigga")
#        break

#2
#i = 6
#while i >= 1:
#    print(i)
#    i -= 1

#3
#i = 1
#while i < 6:
#  print(i)
#  i += 1
#else:
#  print("i is no longer less than 6")

#4

#i = 4

#while i < 10:
#    i += 1
#    if i == 6:
#        continue
#    print(i)

#5
#i = 1
#while i < 10:
#  print(i)
#  if i == 5:
#    break
#  i += 1


#for loops

#1
#i = "gio"
#for x in i:
#    if i[0] == "g":
#        print("shesadzloa es saxeli gio iyos(yvelaze basic saxeli)")
#        break

#2
#iosef  = [1,23,5,4,3,2]

#for i in iosef:
#    if i >= 10:
#        print(f"{i} aris 10ze meti")
#    else:
#        continue

#3
#pc = ["psu","cpu","gpu","ram","ssd","mbo"]

#for parts in pc:
#    if parts == "psu":
#        print("pc has power")
#        break
#    else:
#        print("pc cant turn on cus of no power")
#        break

#4

#dogs = ["chihahua","german shepherd","mozila","linux"]

#for i in dogs:
#    if i == "linux":
#        continue
#    print(i)

#5
#listt = [1,3,4,5,5,9,]
#list2 = []
#for x in range(len(listt)-1):
#    sum = listt[x] + listt[x + 1]
#    print(sum)
#    if sum % 2 == 0:
#        list2.append(sum)

#print(list2)


#if else
#1
#a = 5

#if a >= 5 and a < 10:
#    print("OI THE BUISNESS")
#else:
#    print("..")


#2

#money = 100
#if money >= 100:
#    print("enough for a ticket")
#elif money <= 50:
#    print("enough for a popcorn n drink")
#else:
#    print("not enough")

#3

#age = 10

#if age > 10:
#    print("alpha")
#elif age > 20:
#    print("sigma")
#else:
#    print("idk reebs vwer")

#4 
#age = int(input("please enter your age: "))

#if age >= 1 and age <= 12:
#    print("you are still  a child")
#elif age >= 12 and age < 18:
#    print("you are still a teenager")
#elif age == 0:
#    print("bad input please try again")
#else:
#    print("you are an adult")


#5
#while True:

#    input1 = input("please enter your account name: ")
#    input2 = input("please enter your passowrd: ")
#    name = "luka"
#    password =  "lukita_0301"
#    if input1 == name and input2 == password:
#        print("correct")
#        break
#    else:
#        print("its not correct try again later")