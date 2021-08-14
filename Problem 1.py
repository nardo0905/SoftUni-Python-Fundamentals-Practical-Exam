username = input()

command = input()

while not command == 'Sign up':
    command_data = command.split(' ')
    command_type = command_data[0]

    if command_type == 'Case':
        case_type = command_data[1]
        if case_type == 'lower':
            username = username.lower()
        if case_type == 'upper':
            username = username.upper()
        print(username)

    if command_type == 'Reverse':
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        if start_index < 0 or end_index > len(username):
            command = input()
            continue
        to_reverse = username[start_index:end_index + 1]
        to_reverse = to_reverse[::-1]
        print(to_reverse)

    if command_type == 'Cut':
        substring = command_data[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    if command_type == 'Replace':
        char = command_data[1]
        username = username.replace(char, '*')
        print(username)

    if command_type == 'Check':
        char = command_data[1]
        if char in username:
            print('Valid')
        else:
            print(f'Your username must contain {char}.')

    command = input()
