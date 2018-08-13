from datetime import datetime
from datetime import date
from datetime import timedelta

print(datetime.today())
print(datetime.date())

christmas = date(2018, 12, 25)
todaydate = date.today()

print(str((christmas - todaydate).days))

eta = timedelta(hours=20)

print(str(today + eta))
