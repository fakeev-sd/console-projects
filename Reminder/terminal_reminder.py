import time

reminder = input("О чём вам напомнить? ")
local_time = float(input("Через сколько минут? "))

local_time = local_time * 60

time.sleep(local_time)

print(f"Напоминаю: {reminder}")
