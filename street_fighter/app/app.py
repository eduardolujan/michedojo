
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Location:
    x: int
    y: int


class Movement(ABC):
    """Movement"""

    @abstractmethod
    def move(self, loc: Location) -> Location:
        """Move"""
        raise NotImplementedError(f"Not implemented yet")


class Up(Movement):
    """ Up movement"""

    def move(self, loc: Location):
        """Up move"""
        loc.y = 0
        print('up')
        return loc


class Down(Movement):
    """Down movement"""

    def move(self, loc: Location):
        """Down move"""
        loc.y = 1
        print('down')
        return loc


class Right(Movement):
    """Right movement"""

    def move(self, loc: Location):
        """Down move"""
        loc.x = 0 if loc.x == 4 else loc.x + 1
        print('right')
        return loc


class Left(Movement):
    """Left movement"""

    def move(self, loc: Location):
        """Left move"""
        loc.x = 5 if loc.x == 0 else loc.x - 1
        print('left')
        return loc


class FactoryMovement:
    """FactoryMovement"""

    @staticmethod
    def create(mov: str, loc: Location):
        """Create"""
        factory_dict = dict(
            w=Up,
            s=Down,
            a=Left,
            d=Right
        )
        _class = factory_dict.get(mov)
        instance = _class()
        return instance.move(loc)


class Printer:
    def __init__(self, fighters: List):
        self.fighters = fighters

    def __call__(self, loc: Location):
        for y, row in enumerate(self.fighters):
            for x, figther in enumerate(row):
                if loc.x == x and loc.y == y:
                    print(f"[*{figther}]", end="")
                else:
                    print(f"[{figther}]", end="")
            print("")


class StreetFighter:
    """StreetFighter"""

    fighters = [
        ["Ryu", "Honda", "Blanka", "Guile", "Balrog", "Vega"],
        ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]

    def __init__(self, loc: Location = Location(0, 0)):
        self.loc = loc
        self.printer = Printer(self.fighters)

    def play(self):
        print("Press the w (up), s (down), a (left), d (right) keys to select or press the e key to exit: ")

        key = None
        self.printer(self.loc)
        while key != "e":
            key = input()
            key = ""+key[0]
            loc = FactoryMovement.create(key, self.loc)
            self.printer(loc)


if __name__ == '__main__':
    StreetFighter().play()
