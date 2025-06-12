text1 = "результат операции: 42"
element_index = (text1.index(": "))
number = int(text1[element_index + 1:])
count1 = number + 10
print(count1)

text2 = "результат операции: 514"
element_index = (text2.index(": "))
number = int(text2[element_index + 1:])
count2 = number + 10
print(count2)

text3 = "результат работы программы: 9"
element_index = (text3.index(": "))
number = int(text3[element_index + 1:])
count3 = number + 10
print(count3)
