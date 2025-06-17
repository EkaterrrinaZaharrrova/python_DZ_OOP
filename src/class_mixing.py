class PrintConsoleMixing:
    """Класс вывода в консоль."""

    def __init__(self):
        self.show_info()
        super().__init__()

    def show_info(self):
        print(f'{self.__class__.__name__} ("{self.name}", {self.description}, {self.price}, {self.quantity})')

    def __repr__(self):
        print(f'{self.__class__.__name__} ("{self.name}", {self.description}, {self.price}, {self.quantity})')