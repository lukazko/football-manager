class Team:
    def __init__(self, name):
        self.name = name        
        self.left_striker = None
        self.right_striker = None
        self.left_defender = None
        self.right_defender = None
        self.goalkeeper = None

    def get_players(self):
        team = {"left striker": self.left_striker.name,
                "right striker": self.right_striker.name,
                "left defender": self.left_defender.name,
                "right defender": self.right_defender.name,
                "goalkeeper": self.goalkeeper.name}
        return team

    def add_left_striker(self, left_striker):
        if self.left_striker == None:  
            self.left_striker = left_striker
            left_striker.set_free(0)            
            return 'Přidán jako levý útočník'
        else:
            self.left_striker.set_free(1)
            self.left_striker = left_striker
            left_striker.set_free(0)
            return 'Nahrazen levý útočník' 

    def add_right_striker(self, right_striker):
        if self.right_striker == None:
            self.right_striker = right_striker
            right_striker.set_free(0)
            return 'Přidán jako pravý útočník'
        else:
            self.right_striker.set_free(1)
            self.right_striker = right_striker
            right_striker.set_free(0)
            return 'Nahrazen pravý útočník' 
   
    def del_left_striker(self):
        if self.left_striker == None:
            return 'Není koho odstranit'
        else:
            self.left_striker.set_free(1)
            self.left_striker = None
            return 'Odstraněn levý útočník'  

    def del_right_striker(self):
        if self.right_striker == None:
            return 'Není koho odstranit'
        else:
            self.right_striker.set_free(1)
            self.right_striker = None
            return 'Odstraněn pravý útočník'              