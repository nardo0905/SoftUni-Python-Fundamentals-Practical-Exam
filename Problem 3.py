people = {}
command = input()

while not command == 'Results':
    command_data = command.split(':')
    command_type = command_data[0]

    if command_type == 'Add':
        name = command_data[1]
        health = int(command_data[2])
        energy = int(command_data[3])

        if name not in people:
            people[name] = {'health': health, 'energy': energy}
        else:
            people[name]['health'] += health

    if command_type == 'Attack':
        attacker = command_data[1]
        defender = command_data[2]
        damage = int(command_data[3])

        if attacker in people and defender in people:
            people[defender]['health'] -= damage
            people[attacker]['energy'] -= 1

            if people[defender]['health'] <= 0:
                del people[defender]
                print(f'{defender} was disqualified!')
                command = input()
                continue

            if people[attacker]['energy'] <= 0:
                del people[attacker]
                print(f'{attacker} was disqualified!')

    if command_type == 'Delete':
        username = command_data[1]

        if username == 'All':
            people.clear()
        else:
            if username in people:
                del people[username]

    command = input()

print(f'People count: {len(people)}')
sorted_result = sorted(people.items(), key=lambda x: (-x[1]['health'], x[0]))
for name, data in sorted_result:
    print(f'{name} - {data["health"]} - {data["energy"]}')
