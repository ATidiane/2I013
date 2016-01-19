import soccersimulator, soccersimulator.settings
from soccersimulator import AbstractStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
class RandomStrategy(AbstractStrategy):
    def __init__(self):
        AbstractStrategy.__init__(self, "Random")
    def compute_strategy(self, state, id_team, id_player):
        return SoccerAction(Vector2D.create_random(),
                            Vector2D.create_random())

team1 = SoccerTeam("team1", [Player("t1j1", RandomStrategy())])
team2 = SoccerTeam("team2", [Player("t2j1", RandomStrategy())])
team3 = SoccerTeam("team3", [Player("t3j1", RandomStrategy())])
match = SoccerMatch(team1, team2)
soccersimulator.show(match)
tournoi = SoccerTournament(1)
tournoi.add_team(team1)
tournoi.add_team(team2)
tournoi.add_team(team3)
soccersimulator.show(tournoi)
