class Student:
    def __init__(self):
        self.__id=123

s1=Student()
# print(s1.id)              # Can not be accessed because it is hidden or private
print(s1._Student__id)      # Hidden or private field can be accessed with object name dot underscore
                            # class name and that hidden or private field