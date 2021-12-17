import Stack

stack = Stack.Stack()
_str = input()
not_emp = True

br_open = "("
br_close = ")"

for i in _str:
    if i == br_open:
        stack.push_item(i)
    if i == br_close and not(stack.empty()):
        stack.remove_item()
    elif i == br_close and stack.empty():
        not_emp = False
        break

if not_emp and stack.empty():
    print("Правильно")
else:
    print("Неправльно")