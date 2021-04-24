import csv


def register():
    while True:
        username = input('please enter a username: ')
        flag = False
        with open('login_info.csv', 'r', newline='') as login_file:
            csv_reader = csv.DictReader(login_file)
            for row in csv_reader:
                if username in row['username']:
                    flag = True
                    print("there is already someone with this username!")
                    break
        if flag == False:
            while True:
                password = input('please enter a password with more than 4 characters: ')
                if len(password) <= 4:
                    print('too short password!')
                else:
                    break

            with open('login_info.csv', 'a', newline='') as login_file:
                csv_writer = csv.DictWriter(login_file, fieldnames=['username', 'password'])
                csv_writer.writerow({'username': username, 'password': password})
                print("congratulations! you registered successfully.")
                break


def log_in():
    flag = False
    counter = 0
    username = input("please enter your username: ")
    with open('login_info.csv', 'r', newline='') as login_file:
        csv_reader = csv.reader(login_file)
        for row in csv_reader:
            if username == row[0]:
                with open('locked_users.txt','r') as locked_file:
                    for line in locked_file.readlines():
                        if username == line.strip():
                            print('your account is locked!')
                            return
                password = row[1]
                flag = True
                break
        if flag is False:
            print('there is not such a user!')
        else:
            while True:
                entered_password = input('please enter your password: ')
                if entered_password == password:
                    print('welcome')
                    return {'username': username, 'password': password}
                elif counter == 2:
                    print('your account is locked!')
                    with open('locked_users.txt','a') as locked_file:
                        locked_file.write(f'{username}\n')
                    break
                else:
                    print('wrong password!')
                    counter += 1

while True:
    action = input('what do you want to do? 1-register 2-login : ')
    if action == '1':
        register()
    elif action == '2':
        log_in()
    else:
        print('wrong input')

#register()
log_in()

# for row in csv_reader:
#     if username in row[0]:
#         password = input('please enter your password: ')
#         flag = True
#         while True:
#             if password == row[1]:
#                 print('welcome')
#                 return {'username': username, 'password': password}
#             else:
#                 if counter == 2:
#                     print('your account is locked for an hour!')
#                     break
#                 else:
#                     password = input('wrong password! enter your password again:  ')
#                     counter += 1
# if flag is False:
#     print('there is not such a user!')