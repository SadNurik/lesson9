from datetime import datetime, timedelta

now = '2021-9-10'
dt = datetime.strptime(now, '%Y-%m-%d')
result = dt + timedelta(days=1000)
print(result.strftime('%Y-%m-%d'))