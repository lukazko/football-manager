from player import Player
from team import Team
from match import Match
import gc

player01 = Player(1, 'Leo Messi', 90, 60, 23)
player02 = Player(2, 'Cristiano Ronaldo', 90, 58, 26)
player03 = Player(3, 'Pepe', 89, 59, 23)
player04 = Player(4, 'Diego Maradona', 85, 37, 25)
player05 = Player(5, 'Philipp Lahm', 61, 88, 31)
player06 = Player(6, 'Carlos Puyol', 63, 90, 35)
player07 = Player(7, 'Aymeric Laporte', 60, 78, 33)
player08 = Player(8, 'Tomáš Řepka', 56, 75, 30)
player09 = Player(9, 'Gianluigi Buffon', 45, 71, 89)
player10 = Player(10, 'Iker Casillas', 40, 69, 83,)

team1 = Team("Sparta")
team2 = Team("Slavie")

team1.add_left_striker(player01)
team1.add_right_striker(player02)
team1.add_right_defender(player07)
team1.add_left_defender(player08)
team1.add_goalkeeper(player10)

team2.add_left_striker(player03)
team2.add_right_striker(player04)
team2.add_right_defender(player05)
team2.add_left_defender(player06)
team2.add_goalkeeper(player09)

##print(team1.get_players())
##print(team1.get_offensive_coef())
##print(team1.get_defensive_coef())
match1 = Match(team1, team2)
print(match1.play_match())
print(match1.play_match())

for player in Player.get_instances():
    print(player.name, player.id)