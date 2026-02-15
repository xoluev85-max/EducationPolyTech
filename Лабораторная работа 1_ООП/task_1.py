import doctest
from abc import ABC


class Table(ABC):
    def __init__(self, length_cm: float, width_cm: float, material: str):
        """
        Создание и подготовка к работе объекта "Стол".

        :param length_cm: Длина стола в сантиметрах (должна быть > 0)
        :param width_cm: Ширина стола в сантиметрах (должна быть > 0)
        :param material: Материал стола (непустая строка)

        Примеры:
        >>> table = Table(120.0, 60.0, "wood")
        """
        if not isinstance(length_cm, (int, float)):
            raise TypeError("Длина стола должна быть типа int или float")
        if length_cm <= 0:
            raise ValueError("Длина стола должна быть положительным числом")

        if not isinstance(width_cm, (int, float)):
            raise TypeError("Ширина стола должна быть типа int или float")
        if width_cm <= 0:
            raise ValueError("Ширина стола должна быть положительным числом")

        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if material.strip() == "":
            raise ValueError("Материал не может быть пустой строкой")

        self.length_cm = float(length_cm)
        self.width_cm = float(width_cm)
        self.material = material.strip()

    def area_m2(self) -> float:
        """
        Рассчитать площадь столешницы в квадратных метрах.

        :return: Площадь столешницы (м²)

        Примеры:
        >>> table = Table(120, 60, "wood")
        >>> table.area_m2()
        Ellipsis
        """
        return ...

    def move(self, distance_m: float) -> None:
        """
        Переместить стол на заданное расстояние.

        :param distance_m: Расстояние в метрах (должно быть >= 0)
        :return: None

        Примеры:
        >>> table = Table(120, 60, "wood")
        >>> table.move(2.5)
        """
        if not isinstance(distance_m, (int, float)):
            raise TypeError("distance_m должен быть типа int или float")
        if distance_m < 0:
            raise ValueError("distance_m не может быть отрицательным")
        ...

    def paint(self, color: str) -> None:
        """
        Покрасить стол.

        :param color: Цвет (непустая строка)
        :return: None

        Примеры:
        >>> table = Table(120, 60, "wood")
        >>> table.paint("black")
        """
        if not isinstance(color, str):
            raise TypeError("color должен быть строкой")
        if color.strip() == "":
            raise ValueError("color не может быть пустой строкой")
        ...


class Tree(ABC):
    def __init__(self, species: str, height_m: float, age_years: int):
        """
        Создание и подготовка к работе объекта "Дерево".

        :param species: Порода/вид дерева (непустая строка)
        :param height_m: Высота дерева в метрах (должна быть > 0)
        :param age_years: Возраст дерева в годах (должен быть >= 0)

        Примеры:
        >>> tree = Tree("pine", 12.5, 30)
        """
        if not isinstance(species, str):
            raise TypeError("species должен быть строкой")
        if species.strip() == "":
            raise ValueError("species не может быть пустой строкой")

        if not isinstance(height_m, (int, float)):
            raise TypeError("height_m должен быть типа int или float")
        if height_m <= 0:
            raise ValueError("height_m должен быть положительным числом")

        if not isinstance(age_years, int):
            raise TypeError("age_years должен быть типа int")
        if age_years < 0:
            raise ValueError("age_years не может быть отрицательным")

        self.species = species.strip()
        self.height_m = float(height_m)
        self.age_years = age_years

    def grow(self, years: int) -> None:
        """
        "Вырастить" дерево на указанное количество лет.

        :param years: Количество лет (должно быть > 0)
        :return: None

        Примеры:
        >>> tree = Tree("pine", 12.5, 30)
        >>> tree.grow(5)
        """
        if not isinstance(years, int):
            raise TypeError("years должен быть типа int")
        if years <= 0:
            raise ValueError("years должен быть положительным")
        ...

    def is_mature(self, mature_age_years: int) -> bool:
        """
        Проверить, считается ли дерево взрослым.

        :param mature_age_years: Порог взрослости (должен быть >= 0)
        :return: True/False

        Примеры:
        >>> tree = Tree("pine", 12.5, 30)
        >>> tree.is_mature(20)
        Ellipsis
        """
        if not isinstance(mature_age_years, int):
            raise TypeError("mature_age_years должен быть типа int")
        if mature_age_years < 0:
            raise ValueError("mature_age_years не может быть отрицательным")
        return ...

    def prune(self, percent: float) -> None:
        """
        Обрезать крону дерева на процент.

        :param percent: Процент обрезки (0..100)
        :return: None

        Примеры:
        >>> tree = Tree("pine", 12.5, 30)
        >>> tree.prune(15.0)
        """
        if not isinstance(percent, (int, float)):
            raise TypeError("percent должен быть типа int или float")
        if percent < 0 or percent > 100:
            raise ValueError("percent должен быть в диапазоне 0..100")
        ...


class Stack(ABC):
    def __init__(self, capacity: int, current_size: int, name: str):
        """
        Создание и подготовка к работе объекта "Стек" (структура данных).

        :param capacity: Максимальная вместимость стека (должна быть > 0)
        :param current_size: Текущее количество элементов (0..capacity)
        :param name: Имя/назначение стека (непустая строка)

        Примеры:
        >>> stack = Stack(10, 0, "undo_stack")
        """
        if not isinstance(capacity, int):
            raise TypeError("capacity должен быть типа int")
        if capacity <= 0:
            raise ValueError("capacity должен быть положительным")

        if not isinstance(current_size, int):
            raise TypeError("current_size должен быть типа int")
        if current_size < 0:
            raise ValueError("current_size не может быть отрицательным")
        if current_size > capacity:
            raise ValueError("current_size не может быть больше capacity")

        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if name.strip() == "":
            raise ValueError("name не может быть пустой строкой")

        self.capacity = capacity
        self.current_size = current_size
        self.name = name.strip()

    def push(self, items_count: int = 1) -> None:
        """
        Добавить элементы в стек.

        :param items_count: Сколько элементов добавить (должно быть > 0)
        :return: None
        :raise ValueError: если добавление переполняет стек

        Примеры:
        >>> stack = Stack(3, 1, "undo_stack")
        >>> stack.push(1)
        """
        if not isinstance(items_count, int):
            raise TypeError("items_count должен быть типа int")
        if items_count <= 0:
            raise ValueError("items_count должен быть положительным")
        if self.current_size + items_count > self.capacity:
            raise ValueError("Нельзя добавить элементы: стек переполнится")
        ...

    def pop(self, items_count: int = 1) -> int:
        """
        Удалить элементы из стека и вернуть количество реально удалённых.

        :param items_count: Сколько элементов удалить (должно быть > 0)
        :return: Количество удалённых элементов
        :raise ValueError: если в стеке меньше элементов, чем требуется удалить

        Примеры:
        >>> stack = Stack(3, 2, "undo_stack")
        >>> stack.pop(1)
        Ellipsis
        """
        if not isinstance(items_count, int):
            raise TypeError("items_count должен быть типа int")
        if items_count <= 0:
            raise ValueError("items_count должен быть положительным")
        if items_count > self.current_size:
            raise ValueError("Нельзя удалить больше элементов, чем есть в стеке")
        return ...

    def is_empty(self) -> bool:
        """
        Проверить, пустой ли стек.

        :return: True, если стек пустой, иначе False

        Примеры:
        >>> stack = Stack(5, 0, "undo_stack")
        >>> stack.is_empty()
        Ellipsis
        """
        return ...


if __name__ == "__main__":
    doctest.testmod()
