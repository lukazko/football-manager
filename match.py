class Match:
    def __init__(self, team1, team2, team1_goals = '-', team2_goals = '-', played = 0):
        self.team1 = team1
        self.team2 = team2
        self.team1_goals = team1_goals
        self.team2_goals = team2_goals
        self.played = played

    def get_score(self):
        return str(self.team1_goals) + ':' + str(self.team2_goals)

    def play_match(self):
        if self.played == 1:
            return 'Tento zápas je již odehrán'

        team1_oc = self.team1.get_offensive_coef()   
        team1_dc = self.team1.get_defensive_coef()
        team2_oc = self.team2.get_offensive_coef()
        team2_dc = self.team2.get_defensive_coef()

        self.team1_goals = 0
        self.team2_goals = 0

        if team1_oc > team2_dc:
            self.team1_goals = 1

        if team2_oc > team1_dc:
            self.team2_goals = 1

        self.played = 1

        if self.team1_goals > self.team2_goals:
            return 'Vyhrál tým ' + self.team1.name + '. Výsledek ' + self.get_score()
        elif self.team1_goals < self.team2_goals:
            return 'Vyhrál tým ' + self.team2.name + '. Výsledek ' + self.get_score()
        else:
            return 'Remíza. Výsledek ' + self.get_score()


            
             