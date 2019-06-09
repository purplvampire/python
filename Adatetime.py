import datetime
x = datetime.datetime.now()
print(x)

dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
x = dt.year
print(x)
x = dt.month
print(x)
x = dt.day
print(x)

x = datetime.datetime.fromtimestamp(100000)
print(x)

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
x = delta.days
print(x)
x = delta.seconds
print(x)
x = delta.microseconds
print(x)
x = delta.total_seconds()
print(x)
print(delta)

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
x = dt + thousandDays
print(x)

oct21st = datetime.datetime.now()
aboutThirtyYears = datetime.timedelta(days=365 * 30)
x = oct21st - aboutThirtyYears
print(x)

x = oct21st - (2 * aboutThirtyYears)
print(x)

# Time format change
oct21st = datetime.datetime.now()
x = oct21st.strftime('%Y/%m/%d %H:%M:%S')
print(x)
x = oct21st.strftime('%I:%M %p')
print(x)
x = oct21st.strftime('%B of %y')
print(x)

dt = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(dt)
dt = datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(dt)
dt = datetime.datetime.strptime('October of 15', '%B of %y')
print(dt)