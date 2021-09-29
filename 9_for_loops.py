# prices = [10, 20, 30]
# total = 0
#
# for price in prices:
#     total = total + price
# print(f'Total: {total}')
#
#
# # NESTED LOOP
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for num in range(number):
        output += 'x'
    print(output)
print()
for number in numbers:
    print('x' * number)