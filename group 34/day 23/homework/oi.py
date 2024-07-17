#1
# def niga(n):
#     return n + 5

# print(niga(5))


#2
# def oi(n,n1):
#     return n * n1

# print(oi(10,5))

#3
# def niga(n):
#     return len(n)

# print(niga("wewe"))


#4
# def niga(list1):
#     new_list  =[]
#     for x in list1:
#         new_list.append(len(x))

#     return new_list


# print(niga(["qweqwe","eqwe","dasd"]))


#5

# def new(n):
#     if n == n[::-1]:
#         return True
#     else:
#         return False



# print(new("oi"))


#6
# def maxe(n):
#     return max(n,key=len)

# print(maxe(["we","ewewe"]))

#7
# def niga(n):
#     return 1 if (n == 1 or n == 0) else n * niga(n - 1)

# print(niga(23))

#8
# def nigas(n,n1):
#     return max(n) + max(n1)

# print(nigas([23,24],[24,23]))

#9
# def minnigas(n,n1):
#     return min(n) - min(n1)

# print(minnigas([23,24,25],[20,21,22]))


#10
# def niga(n1):
#     return max(n1) - min(n1)

# print(niga([21,20]))

#11
# def niga(n):
#     new_list = []
#     for x in range(len(n)):
#         if x % 2 == 0:
#             new_list.append(n[x])

#     return sum(new_list)

# print(niga([23,24,25,26,27,28]))


#12
# def niga(x):
#     if x % 2 == 0:
#         return "luwia"
#     else:
#         return "kentia"
    
# print(niga(23))

#13
# def niga(n):
#     for x in range(2,(n//2)+1):
#         if (n % x) == 0:
#             return "prime araris"
#         else:
#             return "prime aris"
        

# print(niga(11))


#14
# def niger(n):
#     new_list = []
#     for x in n:
#         new_list.append(x.capitalize())

#     return new_list

# print(niger(["wqe","ewqedas"]))


#15
# def niga(n):
#     odd_list = []
#     even_list = []
#     for x in n:
#         if x % 2 == 0:
#             even_list.append(x // 2)
#         else:
#             odd_list.append(x * 2)
#     return odd_list,even_list

# print(niga([23,24,25,21]))

#16
# def niga(n):
#     return n[::-1].upper()

# print(niga("oi"))

#17
# def niger(n1):
#     odd_list = []
#     even_list = []
#     for x in range(len(n1)):
#         if x % 2 == 0:
#             even_list.append(n1[x].upper())
#         else:
#             odd_list.append(n1[x].upper())
#     return odd_list,even_list
# print(niger(["niga","nigger"]))


#18
# def niger(n):
#     even_list = []
#     odd_list  =[]
#     for x in range(len(n)):
#         if x % 2 == 0:
#             even_list.append(n[x].upper())
#         else:
#             odd_list.append(n[x].capitalize())
#     return odd_list,even_list

# print(niger(["qew","biga"]))


#19
# def niger(n):
#     new_list = []
#     for x in n:
#         if x.islower():
#             new_list.append(x.upper())
#         else:
#             new_list.append(x.lower())

#     return new_list

# print(niger(["qwe","WQE"]))

#20
# def niga(s, substring):
#     index = s.find(substring)
#     if index == -1:
#         return s 
#     elif index % 2 == 0:
#         return s.upper()
#     else:
#         return s.capitalize()
# print(niga("niga","a"))
