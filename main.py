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


player1 = Player('Leo Messi', 90)
player2 = Player('Cristiano Ronaldo', 90)
#print(player1.get_name())
#print(player1.get_overall_rating())

sparta = Team("Sparta", player1, player2)
##print(sparta.get_striker())
##print(sparta.get_goalkeeper())
##print(sparta.get_players())
##print(sparta.get_overall_rating())

player3 = Player('Robin Van Persie', 90)
player4 = Player('David Beckham', 90)
slavie = Team('Slavie', player3, player4)

print(compare(sparta,slavie))
