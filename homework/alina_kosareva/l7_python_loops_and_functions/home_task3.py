text1 = "результат операции: 42"
text2 = "результат операции: 514"
text3 = "результат работы программы: 9"


def new_count(value):
    element_index = value.index(": ")
    number = int(value[element_index + 2:])
    count1 = number + 10
    print(count1)


new_count(text1)
new_count(text2)
new_count(text3)
