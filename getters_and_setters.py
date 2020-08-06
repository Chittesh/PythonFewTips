class Book_enhanced:
    def __init__(self, name, copies):
        self.name = name
        # we are using _ becasue in python its one of the naming convetion to tell that this vatibale should not
        # be accessed directly
        self._copies = copies

    @property
    def copies(self):
        print("Getter is called")
        return self._copies

    @copies.setter
    def copies(self,copies):
        print("Setter is called")
        self._copies = copies

object_book = Book_enhanced("Python",5)
print(object_book.copies)
print("*************************************")
object_book.copies = 10
print("*************************************")
print(object_book.copies)
print("*************************************")

# Getter is called
# 5
# *************************************
# Setter is called
# *************************************
# Getter is called
# 10
# *************************************
