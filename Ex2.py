# Напишите программу, в которой есть суперкласс с приватным текстовым полем. В базовом классе должен быть метод для присваивания значения полю: без параметров и с
# одним текстовым параметром. Объект суперкласса создается передачей одного текстового аргумента конструктору. Доступное только для чтения свойство результатом возвращает
# длину текстовой строки. На основе суперкласса создается подкласс. В подклассе появляется дополнительное открытое целочисленное поле. В классе должны быть такие версии метода
# для присваивания значений полям (используется переопределение и перегрузка метода из суперкласса): без параметров, с текстовым параметром, с целочисленным параметром, с
# текстовым и целочисленным параметром. У конструктора подкласса два параметра (целочисленный и текстовый).

# в рамках одного класса перегрузка методов работает

from multipledispatch import dispatch


class Main:
    __intField = 0
    __strField = ''

    # def __init__(self, strValue, intValue):
    #     self.__strField = strValue
    #     self.__intField = intValue

    @dispatch(str)
    def get_value(self, value):
        self.__strField = value
        return print(f"Вызван из класса: {self.__class__}, значение текстового поля: {self.__strField}")

    @dispatch(int)
    def get_value(self, value):
        self.__intField = value
        return print(f"Вызван из класса: {self.__class__}, значение целочисленного поля: {self.__intField}")


class Secondary(Main):
    __intFieldSecClass = 0
    __strFieldSecClass = ''

    @dispatch(str, int)
    def get_value(self, valueStr, valueInt):
        self.strField = valueStr
        self.intField = valueInt
        return print(
            f"Вызван из класса: {self.__class__}, значение текстового поля: {self.strField}, значение целочисленного поля: {self.intField}")


userInput = Secondary()

try:
    userStr = str(input("Введите строку или оставьте пустым: "))
    userInt = int(input("Введите число или оставьте пустым: "))
except ValueError:
    userInt = None

userInput.get_value(userStr, userInt)

# while True:
#     try:
#         userStr = str(input("Введите строку или оставьте пустым: "))
#         userInt = int(input("Введите число или оставьте пустым: "))
#     except ValueError:
#         userInt = None
#
#     if len(userStr) != 0 and userInt is not None:
#         userInput.get_value(userStr, userInt)
#         break
#     elif len(userStr) == 0 and userInt is not None:
#         userInput.get_value(userInt)
#         break
#     elif userInt is None and len(userStr) != 0:
#         userInput.get_value(userStr)
#         break
#     else:
#         print("Оба аргумента пустыми быть не могут!")
#         continue
