###########################################################
#  Importy tříd a knihoven 
###########################################################

import weakref


###########################################################
#  Definice třídy
###########################################################
class Player:
    _instances = set()

    # Inicializační metoda
    def __init__(self, id, name, shooting, defense, goalkeeping, img, free = 1):
        self.id = id
        self.name = name
        self.shooting = shooting
        self.defense = defense
        self.goalkeeping = goalkeeping
        self.img = img
        self.free = free
        self._instances.add(weakref.ref(self))

    # Metoda pro nastavování obsazenosti hráče
    def set_free(self, status):
        self.free = status

    # Získání odkazů na všechny instance třídy   
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

    # Získání odkazů na všechny instance třídy, navíc musí jít o volné hráče
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