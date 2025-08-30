import datetime

time = "Jan 15, 2023 - 12:05:33"
my_time = datetime.datetime.strptime(time, "%b %d, %Y - %X")
new_time = my_time.strftime("%d.%m.%Y, %I:%M")
month = my_time.strftime("%B")
print(month)
print(new_time)
