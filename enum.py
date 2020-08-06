from Lib import enum


class Enum_Class(enum.Enum):
    USA = 1
    INDIA = 2
    CHINA = 3

print(Enum_Class.USA)           #Enum_Class.USA
print(Enum_Class(1))            #Enum_Class.USA
print(Enum_Class(1).name)       #USA
print(Enum_Class(1).value)      #1


for i in Enum_Class:
    print(i)


