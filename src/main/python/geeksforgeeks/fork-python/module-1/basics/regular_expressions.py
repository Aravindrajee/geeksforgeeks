import re


def regex_magic():
    sentence = 'horses are fast'
    regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
    matches = re.match(regex, sentence)
    print(matches.groupdict())      # prints {'animal': 'horses', 'verb': 'are', 'adjective': 'fast'}


if __name__ == '__main__':
    regex_magic()
