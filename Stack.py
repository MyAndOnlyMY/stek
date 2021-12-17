class Stack:
    __stack = []

    def push_item(self, item):
       self.__stack = [item] + self.__stack

    def pop_item(self):
        tmp = self.__stack[0]
        return tmp

    def remove_item(self):
        self.__stack.remove(self.__stack[0])

    def get_stack(self):
        return self.__stack

    def empty(self):
        if len(self.__stack) == 0:
            return True