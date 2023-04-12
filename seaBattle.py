class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    def __init__(self, bow, len_ship, orintation):
        self.bow = bow
        self.len_ship = len_ship
        self.orintation = orintation
        self.lives = len_ship
    
    @property
    def dots(self):
        ship_dots = []
        for i in range(self.len_ship):
            cur_x = self.bow.x
            cur_y  = self.bow.y

            if self.orintation == 0:
                cur_x += i
            elif self.orintation == 1:
                cur_y += i
            
            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots
    
    def shooten(self, shot):
        return shot in self.dots
    





class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы вышли за доску!"

class BoardUseException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):
    pass

class Board:
    def __init__(self, hid = False, size = 6):
        self.size = size 
        self.hid = hid 

        self.count = 0
        
        self.field = [["0"]*size for _ in range(size)]

        self.busy = []
        self.ships = []
    
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"

        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " |"
        
        if self.hid:
            res = res.replace("#", "0")
        return res 

b = Board()
print(b)