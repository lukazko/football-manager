###########################################################
#  Definice třídy
###########################################################

class Team:

    # Inicializační metoda
    def __init__(self, name, left_striker = None, right_striker = None, left_defender = None, right_defender = None, goalkeeper = None):
        self.name = name        
        self.left_striker = left_striker
        self.right_striker = right_striker
        self.left_defender = left_defender
        self.right_defender = right_defender
        self.goalkeeper = goalkeeper

    # Metoda pro získání slovníku se sestavou týmu
    def get_players(self):
        team = {"left striker": self.left_striker.name,
                "right striker": self.right_striker.name,
                "left defender": self.left_defender.name,
                "right defender": self.right_defender.name,
                "goalkeeper": self.goalkeeper.name}
        return team

    # Metoda pro přidání levého útočníka do týmu  
    def add_left_striker(self, left_striker):
        if self.left_striker == None:  
            self.left_striker = left_striker
            left_striker.set_free(0)            
            return left_striker.name + ' přidán jako levý útočník.'
        else:
            self.left_striker.set_free(1)
            self.left_striker = left_striker
            left_striker.set_free(0)
            return left_striker.name + ' je nový levý útočník.' 

    # Metoda pro přidání pravého útočníka do týmu  
    def add_right_striker(self, right_striker):
        if self.right_striker == None:
            self.right_striker = right_striker
            right_striker.set_free(0)
            return right_striker.name + ' přidán jako pravý útočník.'
        else:
            self.right_striker.set_free(1)
            self.right_striker = right_striker
            right_striker.set_free(0)
            return right_striker.name + ' je nový pravý útočník'

    # Metoda pro přidání levého obránce do týmu    
    def add_left_defender(self, left_defender):
        if self.left_defender == None:  
            self.left_defender = left_defender
            left_defender.set_free(0)            
            return left_defender.name + ' přidán jako levý obránce.'
        else:
            self.left_defender.set_free(1)
            self.left_defender = left_defender
            left_defender.set_free(0)
            return left_defender.name + ' je nový levý obránce.' 

    # Metoda pro přidání pravého obránce do týmu    
    def add_right_defender(self, right_defender):
        if self.right_defender == None:
            self.right_defender = right_defender
            right_defender.set_free(0)
            return right_defender.name + ' přidán jako pravý obránce.'
        else:
            self.right_defender.set_free(1)
            self.right_defender = right_defender
            right_defender.set_free(0)
            return right_defender.name + ' je nový pravý obránce.'             
   
    # Metoda pro přidání brankáře do týmu    
    def add_goalkeeper(self, goalkeeper):
        if self.goalkeeper == None:
            self.goalkeeper = goalkeeper
            goalkeeper.set_free(0)
            return goalkeeper.name + ' přidán jako brankář.'
        else:
            self.goalkeeper.set_free(1)
            self.goalkeeper = goalkeeper
            goalkeeper.set_free(0)
            return goalkeeper.name + ' je nový brankář.'  

    # Metoda pro odebrání levého útočníka z týmu
    def del_left_striker(self):
        if self.left_striker == None:
            return 'Není koho odstranit'
        else:
            self.left_striker.set_free(1)
            self.left_striker = None
            return 'Odstraněn levý útočník'  

    # Metoda pro odebrání pravého útočníka z týmu
    def del_right_striker(self):
        if self.right_striker == None:
            return 'Není koho odstranit'
        else:
            self.right_striker.set_free(1)
            self.right_striker = None
            return 'Odstraněn pravý útočník'

    # Metoda pro odebrání levého obránce z týmu
    def del_left_defender(self):
        if self.left_defender == None:
            return 'Není koho odstranit'
        else:
            self.left_defender.set_free(1)
            self.left_defender = None
            return 'Odstraněn levý obránce'  

    # Metoda pro odebrání pravého obránce z týmu
    def del_right_defender(self):
        if self.right_defender == None:
            return 'Není koho odstranit'
        else:
            self.right_defender.set_free(1)
            self.right_defender = None
            return 'Odstraněn pravý obránce'  

    # Metoda pro odebrání brankáře z týmu
    def del_goalkeeper(self):
        if self.goalkeeper == None:
            return 'Není koho odstranit'
        else:
            self.goalkeeper.set_free(1)
            self.goalkeeper = None
            return 'Odstraněn brankář' 

    # Metoda pro získání ofenzivního koeficientu týmu
    def get_offensive_coef(self):
        ls = self.left_striker.shooting  
        rs = self.right_striker.shooting
        ld = self.left_defender.shooting
        rd = self.right_defender.shooting
        gk = self.goalkeeper.shooting

        return 3 * (ls + rs) + ld + rd + 0.5 * gk
    
    # Metoda pro získání defenzivního koeficientu týmu
    def get_defensive_coef(self):
        ls = self.left_striker.defense  
        rs = self.right_striker.defense
        ld = self.left_defender.defense
        rd = self.right_defender.defense
        gk = self.goalkeeper.defense + 2 * self.goalkeeper.goalkeeping

        return 0.5 * (ls + rs) + 2 * (ld + rd) + gk

    # Metoda pro kontrolu, zda je tým kompletně sestavený
    def is_complete(self):
        if self.left_defender is not None and self.left_striker is not None and self.right_striker is not None and self.right_defender is not None and self.goalkeeper is not None:
            return True
        else:
            return False     