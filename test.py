from soccersimulator import show
from soccersimulator import SoccerMatch
from team import team1, team2, team4

match_team1 = SoccerMatch(team1, team1)
match_team2 = SoccerMatch(team2, team2)
match_team4 = SoccerMatch(team4, team4)

if __name__ == "__main__":
    show(match_team1)
