import hashlib
import time
import timeit
# from humanfriendly import format_timespan

password = input()

start = timeit.default_timer()
sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
stop = timeit.default_timer()
execution_time = stop - start

start1 = timeit.default_timer()
md5password = hashlib.md5(password.encode('utf-8')).hexdigest().upper()
stop1 = timeit.default_timer()
execution_time1 = stop1 - start1

print(password)
print(len(password))
print(sha1password)
print(md5password)
print("Program Executed in SHA1",execution_time)
print("Program Executed in MD5",execution_time)
# print("Total execution time: ", format_timespan(end_time))