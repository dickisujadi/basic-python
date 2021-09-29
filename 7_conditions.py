# # # # is_hot = False
# # # # is_cold = False
# # # #
# # # # if is_hot:
# # # #     print("It's a hot day")
# # # #     print("Drink plenty of water")
# # # # elif is_cold:
# # # #     print("It's a cold day")
# # # #     print("Wear warm clothes")
# # # # else:
# # # #     print("It's a lovely day")
# # # # print("Enjoy your day")
# # #
# # # TEST CASE 1
# # # price = 1000000
# # # good_credit = False
# # # down_payment = 0
# # #
# # # if good_credit:
# # #     down_payment = 0.1 * price
# # # else:
# # #     down_payment = 0.2 * price
# # # print(f'your down payment ${down_payment}')
# #
# # # TEST CASE 2
# # # has_high_income = True
# # # has_good_credit = False
# # #
# # # if has_high_income or has_good_credit:
# # #     print("Eligible for loan")
# #
# # has_high_income = True
# # has_criminal_record = False
# #
# # if has_high_income and not has_criminal_record:
# #     print("Eligible for loan")
#
# # Test Case 3 :
# name = 'Di'
# if len(name) < 3:
#     print('Name must be at least 3 characters')
# elif len(name) > 50:
#     print('Name can be a maximum of 50 characters')
# else:
#     print("Name looks good")

# Test Case 4 :
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
if(unit.lower() == 'l'):
    weight = int(weight) * 0.45
    print(f"You are {'%.2f' % weight} kilograms")
elif(unit.lower() == 'k'):
    weight = int(weight) * 2.2
    print(f"You are {'%.2f' % weight} pounds")
else:
    print("Sorry, wrong unit")
