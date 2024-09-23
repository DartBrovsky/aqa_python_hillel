import time
from datetime import datetime, date, timedelta

current_day_last = 365
print(date.fromordinal(current_day_last))

current_day: int = date.today().toordinal()
print(current_day)


current_day: int = datetime.strptime("2024-09-23", "%Y-%m-%d").toordinal()
print(current_day)

epoch_current_time: float = time.time()
print(epoch_current_time)

current_date_time: datetime = datetime.fromtimestamp(epoch_current_time)
print(current_date_time)


print(date.today())
print(datetime.today())

print(datetime.now())

print(datetime.strftime(current_date_time, "%Y-%m-%d"))
print(datetime.strptime("2024-09-23", "%Y-%m-%d"))

print(datetime.isoformat(current_date_time))

print(datetime.replace(current_date_time, year=1999, month=2))

print(datetime.weekday(current_date_time))

# timedelta class

current_time: datetime = datetime.now()

time.sleep(5)
current_time_plus_5_seconds: datetime = datetime.now()
#
print(current_time)
print(current_time_plus_5_seconds)
#
difference: timedelta = current_time_plus_5_seconds - current_time
print(difference)
# print(current_time + timedelta(seconds=5))

if difference == timedelta(seconds=5, microseconds=4327):
    print("OKAY")

