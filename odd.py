from datetime import datetime
import time
import random

oddList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
           31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# print(right_now_time)
for num in range(5):
    right_now_time = datetime.today().minute
    if right_now_time in oddList:
        print('奇数分です')
    else:
        print('偶数分です')

    if num == 4:
        break

    time.sleep(random.randint(5, 10))
