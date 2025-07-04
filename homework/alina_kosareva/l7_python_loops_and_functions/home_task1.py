# Старый вариант:
# num = 5
# user_num = int(input("Enter your number: "))
# while user_num != 5:
#     print("Попробуйте снова")
#     user_num = int(input("Enter your number: "))
# print("Поздравляю! Вы угадали!")

num = 5

while True:
    user_num = int(input("Enter your number: "))
    if user_num != num:
        print("Попробуйте снова")
    else:
        break

print("Поздравляю! Вы угадали!")
