# a.
import time

time_start = time.time()
for x in range(1, 7):
    for z in range(1, 21):
        y = (100 - 15 * x - 5 * z) / 2
        if x > 0 and z > 0 and y > 0:
            if (100 - 15 * x - 5 * z) % 2 == 0:
                print(x, int(y), z, 15 * x + 2 * y + 5 * z)
time_end = time.time()
print('执行时间:', time_end-time_start)





