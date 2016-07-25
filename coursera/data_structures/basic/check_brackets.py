import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def is_balanced(text):
    stack = []
    opening = ['(', '[', '{']
    closing = [')', ']', '}']

    for i, c in enumerate(text):
        if c in opening:
            stack.append(Bracket(c, i))
        elif c in closing:
            if len(stack) == 0:
                return False, [Bracket(c, i)]
            top = stack.pop()

            if not top.Match(c):
                return False, [Bracket(c, i)]

    return len(stack) == 0, stack


if __name__ == "__main__":
    text = sys.stdin.read()

    ans = 'Success'

    balanced, remaining_stack = is_balanced(text[:-1])

    if not balanced:
        print(remaining_stack[0].position + 1)
    else:
        print(ans)
