from soccersimulator import SoccerTeam, Player
from coordination import *

t1j1 = Player("t1j1", attaquante)
lalya1 = SoccerTeam("lalya1", [t1j1])
moi = Player("moi", gardien)
lalya1bis = SoccerTeam("lalya1bis", [moi])

t2j1 = Player("t2j1", gardien)
t2j2 = Player("t2j2", attaquante)
lalya2 = SoccerTeam("lalya2", [t2j1, t2j2])

t4j1 = Player("t4j1", defenseur)
t4j2 = Player("t4j2", attaquant)
t4j3 = Player("t4j3", gardien_team4)
t4j4 = Player("t4j4", attaquante)
lalya4 = SoccerTeam("lalya4", [t4j1, t4j2, t4j3, t4j4])
