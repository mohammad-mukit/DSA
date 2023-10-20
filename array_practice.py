# import time

# expense_list = [['January', 2200],
#                 ['February', 2350],
#                 ['March', 2600],
#                 ['April', 2130],
#                 ['May', 2190],
#                 ]

# #extra cost from January
# extrainFeb = expense_list[1][1]-expense_list[0][1]
# print(f'{extrainFeb} is extra cost')

# #total expense
# totalthreemonths = expense_list[0][1]+expense_list[1][1]+expense_list[2][1]
# print(f'Total in first quarter is {totalthreemonths}')

# #check expense in months is 2000
# for item in expense_list:
#     if item[1] == 2000:
#         print(f'{item[0]} expense is 2000 dollars')

# #June expense added
# expense_list.append(['June', 1980])
# print(expense_list)


# #return and refund added
# for item in expense_list:
#     if item[0] == 'April':
#         item[1] += 200
# print(expense_list)

#####################################################

# #creating a list of odd numbers till max number

# mylist = []
# max_num = int(input('Enter a Number: '))

# for i in range(max_num):
#     if i % 2 != 0:
#         mylist.append(i)
# print(mylist)

#######################################################

# #create a list of prime numbers till a given number
# primenumber = [2]
# given_num = int(input('Enter a number: '))

# def isPrime(num):
#     prime = None
#     if num == 0 or num == 1:
#         return False
    
#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#             break
#         else:
#             prime = True

#     return prime

# for i in range(given_num):
#     if isPrime(i):
#         primenumber.append(i)
#     else:
#         continue
    
# print(primenumber)

########################################################
