
def method1():
    print("Module 1 method 1")

class Class_method1:
    def class_method1(self):
        print("Class method 1")

print(__name__)

# method1()                           #Module 1 method 1
# Class_method1().class_method1()     #Class method 1

if __name__ == '__main__':
    method1()
    Class_method1().class_method1()
#__main__
#Module 1 method 1
#Class method 1

