from soccersimulator import SoccerTeam, Player
from coordination import *

t1j1 = Player("t1j1", attaquant)
lalya1 = SoccerTeam("team1", [t1j1])

t2j1 = Player("t2j1", gardien)
t2j2 = Player("t2j2", attaquant)
lalya2 = SoccerTeam("team2", [t2j1, t2j2])

t4j1 = Player("t4j1", gardien)
t4j2 = Player("t4j2", defenseur)
t4j3 = Player("t4j3", attaquant)
t4j4 = Player("t4j4", attaquant)
lalya4 = SoccerTeam("team4", [t4j1, t4j2, t4j3, t4j4])
