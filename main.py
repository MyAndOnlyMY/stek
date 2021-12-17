import Stack

stack1 = Stack.Stack()
stack2 = Stack.Stack()
stack3 = Stack.Stack()
_str_f = input()
_str = ""
not_emp1 = True
not_emp2 = True
not_emp3 = True

br_open1 = "("
br_close1 = ")"
br_open2 = "["
br_close2 = "]"
br_open3 = "{"
br_close3 = "}"


for i in _str_f:
    if i == br_open1 or i == br_close1:
        _str += i

for i in _str:
    if i == br_open1:
        stack1.push_item(i)
    if i == br_close1 and not(stack1.empty()):
        stack1.remove_item()
    elif i == br_close1 and stack1.empty():
        not_emp1 = False
        break


# for i in _str:
#     if i == br_open1

if not_emp1 and stack1.empty():
    print("Правильно")
else:
    print("Неправльно")