students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students),'study these subjects:',', '.join(subjects))

# my_text = 'Students %s study these subjects: %s'
# print(my_text % (", ".join(students),", ".join(subjects)))

# string format
# my_text = 'Students {0} study these subjects: {1}'
# print(my_text.format(", ".join(students),", ".join(subjects)))

# f-string
# print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')
