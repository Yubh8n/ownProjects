from datetime import datetime

hour = datetime.now().hour
min = datetime.now().minute

interval    = 180 + 38 # mins
stop_hour   = 0
stop_min    = 0

stop_hour   = hour + int(((min+interval) / 60))
stop_min    = (min + interval) % 60

print(stop_hour , ":", stop_min)

