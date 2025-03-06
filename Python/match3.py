import re
regex = r'^The'
strings = 'The quick brown fox', 'The lazy dog', 'A quick brown fox'
for string in strings:
    if re.match(regex, string):
        print(f'Match:{string}')
    else:
        print(f'Not Match:{string}')

