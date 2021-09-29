# # # # # names = ['John', 'Bob', 'Mosh', 'Sarah', 'Marry']
# # # # # print(names)
# # # # # print(names[1])
# # # # # print(names[-1])
# # # # # print(names[2:4])
# # # # # print(names[2:])
# # # # # print(names[:4])
# # # #
# # # # numbers = [1,2,8,4,5]
# # # # biggest = numbers[0]
# # # # for number in numbers:
# # # #     if number > biggest:
# # # #         biggest = number
# # # # print(biggest)
# # #
# # # matrix = [
# # #     [1,2,3],
# # #     [4,5,6],
# # #     [7,8,9]
# # # ]
# # #
# # # for row in matrix:
# # #     print([])
# # #     for item in row:
# # #         print(item)
# #
# # numbers = [2,5,2,7,10]
# # numbers.append(20)
# # print(numbers)
# # numbers.insert(2, 9)
# # print(numbers)
# # numbers.remove(7)
# # print(numbers)
# # print(numbers.index(2))
# # print(50 in numbers)
# # numbers.pop()
# # print(numbers)
# # numbers.sort()
# # print(numbers)
# # numbers.reverse()
# # print(numbers)
# # print(numbers.count(2))
# # numbers.clear()
# # print(numbers)
# #
# #
# numbers = [4,5,6,7,8,4,5,6,8,9]
# unique = []
# for number in numbers:
#     if numbers.count(number) == 1:
#         unique.append(number)
# print(unique)

# TUPLE
# INSTEAD OF DOING THIS
coordinates = (1,2,3)
a = coordinates[0]
b = coordinates[1]
c = coordinates[2]
print(f'{a}, {b}, {c}')

# DO THIS - THIS IS TUPLE
x,y,z = coordinates
print(f'{x}, {y}, {z}')