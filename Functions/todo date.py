import datetime


n = datetime.datetime.now()

f = (n)
y = (n.year)
m = (n.month)
d = (n.day)

s = int(input("Enter your year:")) 
z = y - s

n = int(input("Enter you month:"))
if (n < m):
    p = m - n
else:
    p = n - m

e = int(input("Enter you date:"))
if (e < d):
    g = d - e
else:
    g = e -d

print("The duration is:",z,"Years",p,"months",g,"days")