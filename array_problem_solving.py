
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

