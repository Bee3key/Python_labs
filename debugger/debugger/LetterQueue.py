__author__ = 'Bogard'

import re

class LILO():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            self.items.pop(0)
        except IndexError:
            pass

    def show(self):
        return self.items


def letter_queue(commands):
    result = ""
    stack = LILO()

    if len(commands) == 0:
        return result

    for command in commands:
        if re.match(r'^PUSH', command):
            value = re.split(r'\s', command)
            stack.push(value[1])
        elif re.match(r'^POP', command):
            stack.pop()

    result = ''.join(stack.show())
    return result

print(letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]))

