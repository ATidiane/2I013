from soccersimulator import SoccerTeam, Player
from coordination import AllStrategy

t1j1 = Player("t1j1", AllStrategy())
team1 = SoccerTeam("team1", [t1j1])

t2j1 = Player("t2j1", AllStrategy())
t2j2 = Player("t2j2", AllStrategy())
team2 = SoccerTeam("team2", [t2j1, t2j2])

t4j1 = Player("t4j1", AllStrategy())
t4j2 = Player("t4j2", AllStrategy())
t4j3 = Player("t4j3", AllStrategy())
t4j4 = Player("t4j4", AllStrategy())
team4 = SoccerTeam("team4", [t4j1, t4j2, t4j3, t4j4])
