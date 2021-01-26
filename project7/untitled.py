import time

date= time.strftime('%A %d-%b-%Y %H:%M:%S %p')
print(date)

time = time.strptime('Saturday 18-Jul-2020 10:09:47:+0530 AM','%A %d-%b-%Y %H:%M:%S:%z %p')
print(time)


z = time.tm_gmtoff
print(z)

# a = time.
# print(a)