import datetime

mytime = datetime.time(13, 20, 1, 20)
print(mytime)
print(mytime.microsecond)
print(type(mytime))

today = datetime.date.today()
print(today)
print(today.ctime())
mydatetime = datetime.datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime)
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)

# DATE
date1 = datetime.date(2021, 11, 3)
date2 = datetime.date(2020, 11, 3)

result = date1 - date2
print(result)

# DATETIME
datetime1 = datetime.datetime(2021, 11, 3, 22, 0)
datetime2 = datetime.datetime(2020, 11, 3, 12, 0)

mydiff = datetime1 - datetime2
print(mydiff)