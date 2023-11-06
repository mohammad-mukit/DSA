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
## program of a game scoreboard record
## useful concept of array based sequence dsa

# class gameEntry:
#     def __init__(self,name,score) -> None:
#         self._name = name
#         self._score = score

#     def get_name(self):
#         return self._name
    
#     def get_score(self):
#         return self._score
    
#     def get_profile(self):
#         return f'{self._name} {self._score}'
    
#     #### this is a very special method __str__ in python. learn it carefully.
#     ## works with the below class comment code
#     # def __str__(self):
#     #     return f'{self._name} {self._score}'
    
    

# class scoreBoard:
#     def __init__(self,capacity) -> None:
#         self._board = [None] * capacity
#         self._n = 0
   

#     def addScore(self,object):
#         score = object.get_score()

#         isValidScore = self._n < len(self._board) or score > self._board[-1].get_score()

#         if isValidScore:
#             if self._n < len(self._board):
#                 self._n += 1
            
#             j = self._n - 1

#             while j > 0 and score > self._board[j-1].get_score():
#                 self._board[j] = self._board[j-1]
#                 j -= 1
#             self._board[j] = object

    
#     def get_info(self):
#         for i in range(self._n):
#             print(self._board[i].get_profile())

#     #### this is a very special method __str__ in python. learn it carefully.
#     ### below code works only with the above class comment part 
#     # def __str__(self):
#     #     return '\n'.join(str(self._board[j])for j in range(self._n))
    

# p1 = gameEntry('Mukit',500)
# p2 = gameEntry('Naima',600)
# p3 = gameEntry('Rafat',700)
# p4 = gameEntry('Raiyan',400)
# p5 = gameEntry('Tahmid',550)
# p6 = gameEntry('Tanya',950)
# # print(p1.__str__())

# s1 = scoreBoard(5)

# s1.addScore(p1)
# s1.addScore(p2)
# s1.addScore(p3)
# s1.addScore(p4)
# s1.addScore(p5)
# s1.addScore(p6)

# print(s1.get_info())


#################################################
## array insert operation internal code 
## how inser operation is performed 

class array:
    def __init__(self,arrsize) -> None:
        self._array = [None] *arrsize

    def get_arrsize(self):
        return len(self._array)
    
    def insert_element(self,index,value):
        if index < len(self._array):
            if self._array[index] == None:
                self._array[index] = value
            else:
                l = len(self._array)
                self._array += [None]
                while l > index:
                    self._array[l] = self._array[l-1]
                    l -= 1
                self._array[l] = value
                
        else:
            self._array += [None] 
            self._array[-1] = value


    def prinarray(self):
        print(self._array)

a1 = array(3)

a1.insert_element(2,5)
a1.insert_element(0,1)
a1.insert_element(1,10)
a1.insert_element(0,20)
a1.insert_element(4,200)
a1.insert_element(2,2000)
a1.insert_element(9,9000)

a1.prinarray()

###########################################