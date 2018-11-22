import re
#test="hi12.i mhi\\n find,thank you.and u, how about u?"
# m=re.findall('hi', test)
# if m:
# 	print(m)
# 	print(type(m))
# else:
# 	print('find nothing')
	
from datetime import date
tod = date.today()
pas = date(2017, 10, 16)
sp = tod - pas
print(sp.days)