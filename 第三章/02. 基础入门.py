from datetime import datetime

# %Y-%m-%d_%H-%M-%S: %Y - 年, %m - 月, %d - 日, %H - 时, %M - 分, %S - 秒
print(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))