class CustomError(Exception):
    """Класс обработки исключений."""

    def __init__(self, *args, **kwargs):
        """Инициализация класса"""

        self.message = args[0] if args else "Ошибка совместимости товаров."

    def __str__(self):
        print(f"{self.message}")
        return self.message