import datetime
now = datetime.datetime.now()
print(now)
print(type(now))

yesterday=datetime.datetime(2019,8,1,0,0,0)
print(yesterday)

howlong=now-yesterday
print(howlong)
print(howlong.days) # Number of days
print(howlong.total_seconds()) # Number of seconds

sometime=datetime.timedelta(days=1)
print(sometime)