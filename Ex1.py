# Напишите программу, в которой есть суперкласс с приватным текстовым полем, конструктором с текстовым параметром и где переопределен метод toString (). На основе
# суперкласса путем наследования создается подкласс. У него появляется еще одно приватное текстовое ноле. Также подкласс должен иметь версии конструктора с одним и
# двумя текстовыми аргументами, а еще в нем должен быть переопределен метод toString (). В обоих классах метод toString () переопределяется так, что он возвращает строку с
# названием класса и значение текстового поля или текстовых полей.

from multipledispatch import dispatch

class Main:

    __strField1 = ''
    __strField2 = ''

    @dispatch(list)
    def toString(self, value):
        self.__strField1 = value
        return __class__, self.__strField1


    @dispatch(list, list)
    def toString(self, value1, value2):
        self.__strField1 = value1
        self.__strField2 = value2
        return __class__, self.__strField1, self.__strField2


class SecondClass(Main):

    __strField3 = ''
    __strField4 = ''

    @dispatch(list)
    def toString(self, value):
        self.__strField3 = value
        return __class__, self.__strField3


    @dispatch(list, list)
    def toString(self, value1, value2):
        self.__strField3 = value1
        self.__strField4 = value2
        return __class__, self.__strField3, self.__strField4


a = SecondClass()
userValue = list(map(str, input("Введите слово(а): ").split()))
print(a.toString(userValue))