# -*-coding: utf8 -*
import soccersimulator
from soccersimulator.settings import *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
import strategy
from strategy import Mystate
class fonceurStrategy(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "fonceur")
    def compute_strategy(self, state, id_team, id_player):
        #si id_team1 à la balle il shoote, sinn il cours juste vers la balle, de même pour id_team2
        mystate = Mystate(state,id_team,id_player)
        if id_team == 1:
            return strategy.gardien(mystate)
        elif id_team == 2:
            return strategy.fonceur(mystate)
        return SoccerAction()
            

team1 = SoccerTeam("team1", [Player("t1j1", fonceurStrategy())])
team2 = SoccerTeam("team2", [Player("t2j1", fonceurStrategy())])
team3 = SoccerTeam("team3", [Player("t3j1", fonceurStrategy())])
match = SoccerMatch(team1, team2)
soccersimulator.show(match)
