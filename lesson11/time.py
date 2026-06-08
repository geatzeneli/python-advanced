import datetime

timeObj = datetime.time(12,30,45,6626)

print(timeObj.hour)
print(timeObj.minute)
print(timeObj.second)
print(timeObj.microsecond)

dateobj = datetime.date(2012,1,1)
print(dateobj.day)
print(dateobj.month)
print(dateobj.year)

specificDate = datetime.datetime(2012,1,1, 3,23,45,66)
formatimiIdates= specificDate.strftime("%Y-%m-%d")
print(formatimiIdates)


utc = datetime.datetime.now(datetime.timezone.utc)
print(utc)

currenttime =datetime.timedelta(hours=3)

customTime= utc.replace(tzinfo=datetime.timezone(currenttime))
print(currenttime)