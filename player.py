import weakref

class Player:
    _instances = set()

    def __init__(self, id, name, shot, defense, goalkeeping, free = 1):
        self.id = id
        self.name = name
        self.shot = shot
        self.defense = defense
        self.goalkeeping = goalkeeping
        self.free = free
        self._instances.add(weakref.ref(self))

    def set_free(self, status):
        self.free = status
    
    @classmethod
    def get_instances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead 

           