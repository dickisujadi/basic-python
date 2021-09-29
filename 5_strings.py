str_1 = 'Python for "you"'
print(str_1)

str_2 = "Python for 'you'"
print(str_2)

str_3 = "Python for you"
       # 0123456789
print(str_3[1])


str_4 = "Python for you"
       # 0123456789
print(str_4[-2])

str_5 = "Python for you"
       # 0123456789
print(str_5[1:-1])

str_6 = '''
    Dear You
    This is the multilines string

    Thank you
    Regards,
    DS
'''
print(str_6)

# FORMATTED STRINGS
first_name = 'Dicki'
last_name = 'Sujadi'
message = first_name + ' [' + last_name + '] is a coder'
msg = f'{first_name} [{last_name}] is a coder'
print(message)
print(msg)

# STRING METHODS
course = 'python for you'
print(len(course))
print(course.capitalize())
print(course.find('for'))
print(course.replace('you', 'me'))

str_bool = True
if(course.find('you')): str_bool = False
print(str_bool)
print('python' in course)