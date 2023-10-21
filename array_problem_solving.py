
#maximum and minimum element of an array
# can be done using max min function but use problem solving methos
# given_array = [22, 14, 8, 17, 35, 3]

# def maxelement(array):
#     max = array[0]
#     for element in array:
#         if element > max:
#             max = element
#         else:
#             continue
#     return max
# print(maxelement(given_array))

# def minelement(array):
#     min = array[0]
#     for element in array:
#         if element < min:
#             min = element
#         else:
#             continue
#     return min
# print(minelement(given_array))

#############################################################

# given_array = [22, 14, 8, 17, 35, 8, 3]

# # recursion method 
# def sortarrayassending(array):
#     lenght = len(array)-1
#     for i in range(lenght):
#         if array[i] > array[i+1]:
#             array[i],array[i+1] = array[i+1],array[i]
#             sortarrayassending(array)
#         else:
#             continue
#     return array

# print(sortarrayassending(given_array))

# #nested loop method
# def sortarrayassending(array):
#     length = len(array)
#     for i in range(length):
#         for j in range(i+1,length):
#             if array[i] > array[j]:
#                 array[i],array[j] = array[j],array[i]
#             else:
#                 continue
#     return array

# print(sortarrayassending(given_array))

#########################################


# given_array = [0,1,0,2,0,1,2,1,0]
# l,m = 0,0
# h = len(given_array)-1

# for i in range(len(given_array)):
#     if given_array[m] == 0:
#         given_array[l],given_array[m] = given_array[m],given_array[l]
#         l += 1
#         m += 1
#     elif given_array[m] == 1:
#         m += 1
#     elif given_array[m] == 2:
#         given_array[m],given_array[h] = given_array[h],given_array[m]
#         h -= 1


# print(given_array)

#########################################


# given_array = [2,5,10,7,8,10]

# target_sum = 35

# def subarr_sum(arr,sum):
#     length = len(arr)
#     temp = 0
#     for i in range(length):
#         temp = arr[i]
#         if temp == sum:
#             pass
#             return f'Sum found at index {i}, which is {arr[i]}'
#         for j in range(i+1,length):
#             temp += arr[j]
#             if temp == sum:
#                 return f'Sum found index between {i} to {j}, which is {arr[i:j+1]}'
#     return 'sum amount not exists'

# print(subarr_sum(given_array,target_sum))

##subarray using given sum using sliding window
# given_array = [15,10,2,8,20]

# def subarrsum(arr,targetsum):
#     length = len(arr)
#     start = 0
#     cursum = arr[0]
#     i = 1
#     while i <= length:
#         while cursum > targetsum:
#             cursum = cursum - arr[start]
#             start +=1
#         if cursum == targetsum:
#             return f'Subarray foun between {start} to {i-1} which is {arr[start:i]}'
#         if cursum < targetsum:
#             cursum = cursum + arr[i]

#         i +=1
#     return 'Subarray not exists'
    
# print(subarrsum(given_array,20))

#############################################################
# maximum sum of n consecutive elements of and array using sliding window

# given_array = [10,12,23,20,22,40,15,20]
# window_size = 3

# def maxsum(arr,size):
#     length  = len(arr)
#     window_sum = sum(arr[:size])
#     maximum_sum = window_sum
#     elements = []
#     for i in range(length-size):
#         window_sum = window_sum - arr[i] + arr[i + size]
#         if maximum_sum >= window_sum:
#             continue
#         else:
#             maximum_sum = window_sum
#             elements = arr[i+1:i+size+1]
#     return f'Maximum some of {size} consecutive elements of the array is {maximum_sum} elements are {elements}'

# print(maxsum(given_array,window_size))


#############################################################
###array medium ploblem solving

## roate array by n element
# given_array = [1,2,3,4,5]
# n = 2
# new_array = given_array[len(given_array)-n:] + given_array[:len(given_array)-n] 
# print(new_array)

# #rotate array by one element
# temp = given_array[len(given_array)-1]
# for i in range(len(given_array)-1,0,-1):
#     given_array[i] = given_array[i-1]

# given_array[0] = temp
# print(given_array)


########################################
## finding missing number from array ranging 1-n, where length off array is n-1.
## thter are many ways to solve this but i prefer cyclic sort tecnique

# given_array = [2,4,1,3,6]

# def findmissingnum(arr):
#     length = len(arr)
#     i = 0

#     while i < length:
#         correc_position = arr[i] - 1
#         if arr[i] < length and arr[i] != arr[correc_position]:
#             arr[i],arr[correc_position] = arr[correc_position],arr[i]
#         else:
#             i += 1

#     for i in range(length):
#         if arr[i] != i + 1:
#             return i + 1

# print(f'the missing number is {findmissingnum(given_array)}')

###########################################
## Count pairs with given sum in an array

# given_array = [1,5,7,-1,5]
# given_sum = 6

# def countpairs(arr,sum):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] + arr[j] == sum:
#                 count += 1
#             else:
#                 continue
#     return count

# print(f'Number of pairs with sum {given_sum} are {countpairs(given_array,given_sum)}')

##############################################

### Count pairs with given sum in an array hashing technique
# given_array = [1,5,7,-1,5,1]
# given_sum = 6

# def countpairs(arr,sum):
#     countlist = {}
#     count = 0
#     for i in range(len(arr)):
#         if sum - arr[i] in countlist:
#             count += countlist[sum - arr[i]]
#         if arr[i] in countlist:
#             countlist[arr[i]] += 1
#         else:
#             countlist[arr[i]] = 1
#     return count
# print(f'Number of pairs with sum {given_sum} are {countpairs(given_array,given_sum)}')

##################################################

## fruits into basket sliding window

# given_array = [1,2,3,4,2,3,2,3,3,3,2,2,4,4,5,5]

# def fruitsintobasket(arr):
#     l = 0
#     maxfruits = 0
#     result = 0
#     fruitslist = {}

#     for i in range(len(arr)):
#         if arr[i] in fruitslist:
#             fruitslist[arr[i]] += 1
#             maxfruits += 1
#         else:
#             fruitslist[arr[i]] = 1
#             maxfruits +=1
#         while len(fruitslist) > 2:
#             f = arr[l]
#             fruitslist[f] -=1 
#             maxfruits -=1
#             l += 1
#             if not fruitslist[f]:
#                 fruitslist.pop(f)
            
#         result = max(result,maxfruits)
#     return result

# print(fruitsintobasket(given_array))

################################################

## find duplicate from a given array within a range n.
## this is the brute force way

# given_array = [1,2,3,6,3,6,1]

# def findduplicate(arr):
#     temp = []
#     temp2 = []
#     for i in range(len(given_array)):
#         if arr[i] in temp:
#             temp2.append(arr[i])
#         else:
#             temp.append(arr[i])
#     temp2.sort()
#     return temp2
# print(findduplicate(given_array))
##################################################