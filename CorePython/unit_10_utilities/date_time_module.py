from datetime import datetime
#from datetime import date
#from datetime import time

# Accessing date/time
current_dt = datetime.now()
print(current_dt) # 2019-12-02 12:45:44.741210
print(str(current_dt))

print("Date: ", current_dt.day,"/", current_dt.month,"/",current_dt.year)
print("Time: ", current_dt.hour,":", current_dt.minute,":",current_dt.second, ":", current_dt.microsecond)

# datetime to timestamp
current_dt = datetime.now()
time_stamp = datetime.timestamp(current_dt)
print(current_dt, "->", time_stamp)

# timestemp to datetime
obj_dt = datetime.fromtimestamp(time_stamp )
print(time_stamp, "->", obj_dt)

# string to datetime
dt1 = "2001-01-23" # yy-mm-dd
dt2 = datetime.strptime(dt1, "%Y-%m-%d")
print(type(dt1))
print(type(dt2))

# date diff
dt1 = "1999-12-22" # yy-mm-dd
dt1 = datetime.strptime(dt1, "%Y-%m-%d")
dt2 = "2019-12-2" # yy-mm-dd
dt2 = datetime.strptime(dt2, "%Y-%m-%d")
diff = dt2 - dt1
print(diff.days/365)