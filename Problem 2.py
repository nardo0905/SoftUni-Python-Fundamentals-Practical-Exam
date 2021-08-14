import re

n = int(input())
matcher = r'^(\$|\%)(?P<tag>[A-Z][a-z]{3,})\1\:\s(\[(?P<num_one>\d+)\])\|(\[(?P<num_two>\d+)\])\|(\[(?P<num_three>\d+)\])\|$'
messages = []

for i in range(0, n):
    message = input()
    check = re.findall(matcher, message)
    valid_message = re.finditer(matcher, message)
    if len(check) > 0:
        for match in valid_message:
            word_one = chr(int(match.group('num_one')))
            word_two = chr(int(match.group('num_two')))
            word_three = chr(int(match.group('num_three')))
            print(f'{match.group("tag")}: {word_one + word_two + word_three}')
    else:
        print('Valid message not found!')
