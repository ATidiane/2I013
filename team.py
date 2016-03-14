from soccersimulator import SoccerTeam, Player
from coordination import *
from decisiontree import gen_features, DTreeStrategy
from myIA import treeStrat

t0 = Player("t0", more_better)
t1 = Player("t1", dribleur)
t2 = Player("t2", passeur)
t3 = Player("t3", z)

moi = Player("moi", gardien)

t1j1 = Player("t1j1", player_team1)
t1j2 = Player("bete", attaquant)

t2j1 = Player("t2j1", gardien)
t2j2 = Player("t2j2", player_team2)

t4j1 = Player("t4j1", defenseur)
t4j2 = Player("t4j2", player_team41)
t4j3 = Player("t4j3", gardien_team4)
t4j4 = Player("t4j4", player_team42)

lalya0 = SoccerTeam("more_better", [t1])
lalya0bis = SoccerTeam("dribleur", [moi])

lalya1 = SoccerTeam("lalya1", [t1j1])
lalya1bis = SoccerTeam("lalya1bis", [moi])

lalya2 = SoccerTeam("lalya2", [t2j1, t2j2])

lalya4 = SoccerTeam("lalya4", [t4j1, t4j2, t4j3, t4j4])

#######################################
# strat IA
#######################################
t1j1IA = Player("IA",treeStrat)
lalya1IA = SoccerTeam("iateam",[t1j1IA])
