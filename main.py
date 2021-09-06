from player import Player
from team import Team

def compare(team1, team2):
    rating1 = team1.get_overall_rating()
    rating2 = team2.get_overall_rating()
    
    if rating1 > rating2:
        return 'Výhrála ' + team1.name
    elif rating1 < rating2:
        return 'Vyhrála' + team2.name
    else:
        return 'Remíza!'

player01 = Player(1, 'Leo Messi', 90, 60)
player02 = Player(2, 'Cristiano Ronaldo', 90, 58)
player03 = Player(3, 'Pepe', 89, 59)
player04 = Player(4, 'Diego Maradona', 85, 37)
player05 = Player(5, 'Philipp Lahm', 61, 88)
player06 = Player(6, 'Carlos Puyol', 63, 90)
player07 = Player(7, 'Aymeric Laporte', 60, 78)
player08 = Player(8, 'Tomáš Řepka', 56, 75,)
player09 = Player(9, 'Gianluigi Buffon', 45, 89)
player10 = Player(10, 'Iker Casillas', 40, 83,)

team1 = Team("Sparta")
team2 = Team("Slavie")

print(team1.add_left_striker(player01))
print(team1.add_left_striker(player02))

print(team1.left_striker.name)
print(team1.del_left_striker())
print(player02.free)