# -*-coding: utf8 -*
import soccersimulator
from soccersimulator.settings import *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
import strategy
from strategy import Mystate


class AllStrategy(BaseStrategy):
    def __init__(self,comportement):
        BaseStrategy.__init__(self,comportement.__name__)
        self.comportement = comportement

    def compute_strategy(self,state, id_team,id_player):
        mystate = Mystate(strategy.miroir_state(state) if id_team != 1 else state,id_team,id_player)
        res = self.comportement(mystate)
        if id_team == 2:
            res = strategy.miroir_socac(res)
            
        return res


attaquant = AllStrategy(strategy.ball_g)

defenseur  = AllStrategy(strategy.defenseur)

gardien = AllStrategy(strategy.gardien)
