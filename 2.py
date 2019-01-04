
import datetime

now_time =  datetime.datetime.now()
str = "hello world: "+datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
print str