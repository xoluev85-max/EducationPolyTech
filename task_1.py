class Animal:
    """Базовый класс животного."""

    def __init__(self, name: str, age: int) -> None:
        """Создает объект животного."""
        self.name: str = name
        self.age: int = age

    def __str__(self) -> str:
        return f"Животное: {self.name}, возраст: {self.age}"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"

    def speak(self) -> str:
        """Животное издает звук."""
        return "Какой-то звук"

    def info(self) -> str:
        """Информация о животном."""
        return f"{self.name}, {self.age} лет"


class Dog(Animal):
    """Класс собаки, наследуется от Animal."""

    def __init__(self, name: str, age: int, breed: str) -> None:
        """Создает объект собаки."""
        super().__init__(name, age)
        self.breed: str = breed

    def __str__(self) -> str:
        return f"Собака: {self.name}, {self.age} лет, порода {self.breed}"

    def __repr__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def speak(self) -> str:
        """
        Переопределение метода.
        У собаки конкретный звук — лай.
        """
        return "Гав!"

    def play(self) -> str:
        """Собака играет."""
        return f"{self.name} играет."