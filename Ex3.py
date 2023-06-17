# Напишите программу, в которой на основе суперкласса создается подкласс, а на основе этого подкласса создается еще один подкласс (цепочка наследования из трех
# классов). В первом суперклассе есть открытое целочисленное поле, метод с одним параметром для присваивания значения полю и конструктор с одним параметром. Во
# втором классе появляется открытое символьное поле, метод с двумя параметрами для присваивания значения полям (перегрузка метода из суперкласса) и конструктор с двумя
# параметрами. В третьем классе появляется открытое текстовое ноле, метод с тремя аргументами для присваивания значений полям (перегрузка метода из суперкласса) и
# конструктор с тремя параметрами. Для каждого класса определите метод toString () так, чтобы он возвращал строку с названием класса и значениями всех полей объекта.


class Superclass:
    def __init__(self, text):
        self._text = text

    def display(self):
        print(f"Class name: {type(self).__name__}, Text: {self._text}")


class IntegerSubclass(Superclass):
    def __init__(self, text, number):
        super().__init__(text)
        self._number = number

    def display(self):
        print(f"Class name: {type(self).__name__}, Text: {self._text}, Number: {self._number}")


class CharSubclass(Superclass):
    def __init__(self, text, char):
        super().__init__(text)
        self._char = char

    def display(self):
        print(f"Class name: {type(self).__name__}, Text: {self._text}, Char: {self._char}")


obj1 = IntegerSubclass("Test text", 10)
obj1.display()

obj2 = CharSubclass("Another text", 'A')
obj2.display()

super_obj = Superclass("Super text")
super_obj.display()

super_obj = obj1
super_obj.display()

super_obj = obj2
super_obj.display()
