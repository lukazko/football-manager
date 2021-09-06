class Player:
    def __init__(self, id, name, shot, defense, free = 1):
        self.id = id
        self.name = name
        self.shot = shot
        self.defense = defense
        self.free = free

    def set_free(self, status):
        self.free = status