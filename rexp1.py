# using regular expression in python
import re
x = 'From stephen.marqwiw@uct.ac.za Sat jan 5, 2018'
y = re.findall('\S+?@\S+',x);
print(y)
