#coding=utf-8

from datetime import datetime, date, timedelta, time
import  time

timestamp = 1462451334

#转换成localtime
time_local = time.localtime(timestamp)
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

print dt
today = date.today();
print(today);
print(date.fromtimestamp(1522561373));  # 将时间戳的日期输出
print(datetime.fromtimestamp(1522561373))
print(date.fromordinal(1));  # 将天数+最小日期 转换成日期输出    0001-01-01
print(date.min);  # 0001-01-01
print(date.max);  # 9999-12-31
print(date.resolution);  # 1 day, 0:00:00

d = date(2017, 1, 4);
d1 = d.replace(year=2016, day=26);
print(d);  # d的值不变，
print(d1);  # 2016-01-26
print(d.toordinal());  # 该日期距离最小日期的天数  736330
print(d.weekday());  # 返回当前日期是所在周的第几天  0 表示周一 6 表示周日
print(d.isoweekday());  # 返回当前日期是所在周的第几天  1 表示周一 7 表示周日
print(d.isocalendar());  # 返回格式如(year，month，day)的元组
print(d.isocalendar()[1]);  # 返回该日期是这一年中的第几周
print(d.isocalendar()[2]);  # 返回该日期是周几
print(d.isoformat());  # 返回 ISO 8601格式  YYYY-MM-DD
print(d.strftime("%d/%m/%y"));  # 04/01/17
print(d.__format__("%d/%m/%y"));  # 04/01/17
print(d.ctime());  # Wed Jan  4 00:00:00 2017