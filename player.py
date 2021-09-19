import weakref

class Player:
    _instances = set()

    def __init__(self, id, name, shoting, defense, goalkeeping, img, free = 1):
        self.id = id
        self.name = name
        self.shoting = shoting
        self.defense = defense
        self.goalkeeping = goalkeeping
        self.img = img
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

    @classmethod
    def get_instances_free(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None and obj.free == 1:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead           