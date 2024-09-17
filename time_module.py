import time
# print(time.time())

t = time.localtime()
c_time = time.strftime("%y-%m-%d %H:%M:%S", t)

print(c_time)
