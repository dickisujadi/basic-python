# # i = 1
# # while i <= 5:
# #     print('*' * i)
# #     i = i + 1
# # print("Done")
#
# guess_count = 1
# guess_limit = 3
# secret_number = 9
# while guess_count<= guess_limit:
#     answer = int(input("Guess: "))
#     if(answer == secret_number):
#         print("Success")
#         break
#     guess_count = guess_count + 1
# else:
#     print("Failed")

cmd_bool = False
cmd = ""
help_cmd = 'help'
start_cmd = 'start'
stop_cmd = 'stop'
quit_cmd = 'quit'
current_cmd = 'stop'

while True:
    cmd = input("Let's Go > ").lower()
    if(cmd == start_cmd and current_cmd != start_cmd):
        current_cmd = start_cmd
        print("The Machine Starts")
    elif (cmd == start_cmd and current_cmd == start_cmd):
        print("The Machine Starts already. Please do something else")
    elif(cmd == stop_cmd and current_cmd != stop_cmd):
        current_cmd = stop_cmd
        print("The Machine Stops")
    elif (cmd == stop_cmd and current_cmd == stop_cmd):
        print("The Machine Stops already. Wanna go somewhere? Start the Machine!")
    elif(cmd == help_cmd):
        print("""help:
    start - to start the car
    stop - to stop the car
    quit - to exit""")
    elif(cmd == quit_cmd):
        break
    else:
        print("Wrong Command")
else:
    print("Bye!")