from Lib import datetime
today = datetime.datetime.today()
print(today)                        #2020-08-06 13:47:03.921283
#to get the value in a human readble format
print(today.__str__())              #2020-08-06 13:47:03.921283
# to get the object representation
print(today.__repr__())             ##datetime.datetime(2020, 8, 6, 13, 47, 3, 921283)



