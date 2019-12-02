import time

local_time = time.strftime(
    "%Y%m%d_%H_%M", time.localtime())  # 格式化為 data_test.csv
print(local_time)
