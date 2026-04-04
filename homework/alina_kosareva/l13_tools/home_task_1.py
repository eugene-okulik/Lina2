import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")
print(data_file_path)


def read_file():
    with open(data_file_path) as data_file:
        for line in data_file.readlines():
            line = line.split(" - ")[0]
            date_str = line.split(" - ")[0].split(". ")[1]
            yield date_str


line = read_file()

first_date = datetime.datetime.strptime(next(line), "%Y-%m-%d %H:%M:%S.%f")
second_date = datetime.datetime.strptime(next(line), "%Y-%m-%d %H:%M:%S.%f")
third_date = datetime.datetime.strptime(next(line), "%Y-%m-%d %H:%M:%S.%f")

print(first_date + datetime.timedelta(days=7))
print(second_date.strftime("%A"))
print((datetime.datetime.now() - third_date).days)
