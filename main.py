from player import Player
from team import Team

def compare():
    pass

player1 = Player('Leo Messi', 90)
player2 = Player('Cristiano Ronaldo', 90)
#print(player1.get_name())
#print(player1.get_overall_rating())

sparta = Team([player1.get_name(), player2.get_name()])
print(sparta.get_players())