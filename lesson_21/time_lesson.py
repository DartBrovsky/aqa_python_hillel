import time
from time import struct_time
from datetime import datetime

current_epoch_time: float = time.time()
current_time: struct_time = time.localtime()

print(time.time())

print(current_time)

print(f"{current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday}-{current_time.tm_hour}-{current_time.tm_min}-{current_time.tm_sec}")
print(time.asctime(current_time))

print(time.ctime(0))
print(time.ctime(current_epoch_time))

print(time.gmtime(current_epoch_time))
print(time.localtime(0))
print(time.localtime(current_epoch_time))

print(time.perf_counter())

# time.sleep(5)

print(time.perf_counter())
print(time.process_time())

print(time.strftime("%a %b %d %H:%M:%S %Y", current_time))

date_time_string: str = time.strftime("%a %b %d %H:%M:%S %Y", current_time)
print(time.strptime(date_time_string, "%a %b %d %H:%M:%S %Y"))

print(time.timezone)
print(time.tzname)

print(time.strftime("%Y-%m-%d %H:%M:%S ", current_time))
print(time.strftime("%Y-%m-%dT%H:%M:%SZ", current_time))

my_date_time = datetime.fromtimestamp(current_epoch_time)
print(my_date_time)


