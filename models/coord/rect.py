class CoordRect:
    x: int = 0
    y: int = 0
    h: int = 0

    def __init__(self, x, y, h=None):
        self.x = int(str(x))
        self.y = int(str(y))
        self.h = int(str(h))

    def __repr__(self) -> str:
        return (f"CoordRect({self.x}, {self.y}, {self.h})"
                )

    def __eq__(self, second):
        return self.x == second.x and self.y == second.y and self.h == second.h

    @property
    def x_str(self) -> str:
        """Возвращает координату X в виде строки (целое число)"""
        return str(int(self.x))

    @property
    def y_str(self) -> str:
        """Возвращает координату Y в виде строки (целое число)"""
        return str(int(self.y))

    @property
    def h_str(self) -> str:
        """Возвращает высоту H в виде строки (целое число)"""
        return str(int(self.h)) if self.h is not None else '0'
