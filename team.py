class Team:
    def __init__(self, name, striker, goalkeeper):
        self.striker = striker
        self.goalkeeper = goalkeeper
        self.name = name

    def get_striker(self):
        return self.striker.get_name()

    def get_goalkeeper(self):
        return self.goalkeeper.get_name()

    def get_players(self):
        team = {"striker": self.striker.get_name(), "goalkeeper": self.goalkeeper.get_name()}
        return team.values()

    def get_overall_rating(self):
        rating = self.striker.get_overall_rating() + self.goalkeeper.get_overall_rating()
        return rating     