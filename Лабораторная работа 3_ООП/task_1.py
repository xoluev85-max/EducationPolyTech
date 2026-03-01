class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        # сохраняем в "приватные" поля, чтобы запретить изменение через property
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if not name.strip():
            raise ValueError("name не может быть пустой строкой")

        if not isinstance(author, str):
            raise TypeError("author должен быть строкой")
        if not author.strip():
            raise ValueError("author не может быть пустой строкой")

        self._name = name.strip()
        self._author = author.strip()

    @property
    def name(self) -> str:
        """Название книги (только чтение)."""
        return self._name

    @property
    def author(self) -> str:
        """Автор книги (только чтение)."""
        return self._author

    def __str__(self) -> str:
        # можно наследовать и PaperBook, и AudioBook — формат общий
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        # валидная python-строка для восстановления объекта.
        # Используем имя реального класса (Book/PaperBook/AudioBook)
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # важно: через property, чтобы отработала валидация

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("pages должен быть int")
        if value <= 0:
            raise ValueError("pages должен быть положительным числом")
        self._pages = value

    def __repr__(self) -> str:
        # расширяем repr, потому что нужно ещё pages
        return (
            f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"
        )


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # через property

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("duration должен быть числом (int или float)")
        value = float(value)
        if value <= 0:
            raise ValueError("duration должен быть положительным числом")
        self._duration = value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
        )
