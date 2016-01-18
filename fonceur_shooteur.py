import soccersimulator
from soccersimulator.settings import *
from soccersimulator import AbstractStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
class fonceurStrategy(AbstractStrategy):
    def __init__(self):
        AbstractStrategy.__init__(self, "fonceur")
    def compute_strategy(self, state, id_team, id_player):
        b = state.ball.position
	p = state.player_state(id_team, id_player)
	distance_joueur_balle = b.distance(p.position)
	rayon_joueur_balle = PLAYER_RADIUS + BALL_RADIUS
	if distance_joueur_balle < rayon_joueur_balle:
	     if id_team == 1:
		  action = SoccerAction(b - p.position, Vector2D(x = GAME_WIDTH, y = GAME_HEIGHT/2.) - state.ball.position)
	     else:
		  action = SoccerAction(b - p.position, Vector2D(x = GAME_HEIGHT/2., y = GAME_WIDTH) - state.ball.position)
	     action_bis = action.copy()
	     action_ter = action + action_bis
	     return SoccerAction(action_ter.acceleration, action_ter.shoot)
	else:
	     return SoccerAction(b - p.position)

team1 = SoccerTeam("team1", [Player("t1j1", fonceurStrategy())])
team2 = SoccerTeam("team2", [Player("t2j1", fonceurStrategy())])
team3 = SoccerTeam("team3", [Player("t3j1", fonceurStrategy())])
match = SoccerMatch(team1, team2)
soccersimulator.show(match)
tournoi = SoccerTournament(1)
tournoi.add_team(team1)
tournoi.add_team(team2)
tournoi.add_team(team3)
soccersimulator.show(tournoi)
