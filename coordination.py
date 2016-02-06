# -*-coding: utf8 -*
import soccersimulator
from soccersimulator.settings import *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
import strategy
from strategy import Mystate


class AllStrategy(BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self, "fonceur")
    def compute_strategy(self, state, id_team, id_player):
        #si id_team1 à la balle il shoote, sinn il cours juste vers la balle, de même pour id_team2
        mystate = Mystate(state,id_team,id_player)
        if id_player == 1:
            return strategy.gardien(mystate)
        else:
            return strategy.fonceur_shooteur(mystate)
