# # # customer = {
# # #     "name": "Dicki Sujadi",
# # #     "email": "dickisujadi@gmail.com",
# # #     "age": 28,
# # #     "is_verified": True,
# # #     "is_active":True
# # # }
# # # print(customer["name"]) # KEY VALUE PAIR MUST BE THE SAME (NOT CASE SENSITIVE) - It doesn't work if name => Name. RETURN ERROR
# # # print(customer.get("birthdate")) # RETURN NONE (NOT ERROR)
# # # print(customer.get("birthdate", "Jan 1 1993"))
# # # customer["name"] = "Jack Smith"
# # # print(customer)
# # #
# # # customer["birthdate"] = "Jan 1 1993"
# # # print(customer)
# # #
# #
# # def handleMember(findNumber):
# #     groups = [{
# #         "groupName": "Group 1",
# #         "groupMembers" : [1,2,3]
# #     },
# #     {
# #         "groupName": "Group 2",
# #         "groupMembers": [3, 4, 8, 9, 10, 11]
# #     },
# #     {
# #         "groupName": "Group 3",
# #         "groupMembers": [3,5,6,7]
# #     }]
# #
# #     # print(groups[0].get("groupName"))
# #     max_groupMembers_amount = 0
# #     groupName = ''
# #     for group in groups:
# #         groupMembers = group.get("groupMembers")
# #         if(findNumber in groupMembers) and (len(groupMembers) > max_groupMembers_amount):
# #             max_groupMembers_amount = len(groupMembers)
# #             groupName = group.get("groupName")
# #     print(groupName)
# #
# # handleMember(3)
#
# msg = input(">")
# words = msg.split(' ')
# emojis = {
#     ":)" : "😊",
#     ":(" : "☹"
# }
# output = ''
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

def handleThis(chars):
    maps = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    probs = list(chars)
    result = []

    for prob in probs:
        result.append(prob)
        if maps.get(prob) != None:
            probs.pop(probs.index(maps.get(prob)))
            result.append(maps.get(prob))

    if len(result)%2 == 0:
        print('success')
    else:
        print('failed')

handleThis('{}[]()')
handleThis('[{()}]')
handleThis('{}][')