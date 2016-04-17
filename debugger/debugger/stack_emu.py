__author__ = 'Bee3Key'

import re

class LILO():

    def __init__(self):
        self.items = []
        self.sum = 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            self.sum = self.sum + self.items.pop()
        except IndexError:
            pass

    def peek(self):
        try:
            self.sum = self.sum + self.items[len(self.items) - 1]
        except IndexError:
            pass

    def show(self):
        return self.sum #self.items


def digit_stack(commands):
    result = 0
    stack = LILO()

    if len(commands) == 0:
        return result

    for command in commands:
        if re.match(r'^PUSH', command):
            value = re.split(r'\s', command)
            stack.push(int(value[1]))
        elif re.match(r'^POP', command):
            stack.pop()
        elif re.match(r'^PEEK', command):
            stack.peek()

    result = stack.show()
    return result


#coms = ["PUSH 9", "PUSH 9", "POP", "PUSH 9"]
#coms = []
coms = ["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]

print(digit_stack(coms))






