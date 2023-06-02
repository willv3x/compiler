class Stack:
    def __init__(self, initial_element=None):
        if initial_element is not None:
            self._stack = [initial_element]
        else:
            self._stack = []

    def top(self):
        return self._stack[-1]

    def stack_up(self, element):
        self._stack.append(element)

    def unstack(self, element_number):
        unstacked = []
        for _ in range(element_number):
            unstacked.append(self._stack.pop())
        return unstacked

    def get(self):
        return self._stack

    def get_first_match(self, match):
        for element in reversed(self._stack):
            if element.classe == match:
                return element
