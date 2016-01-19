import soccersimulator
from soccersimulator.settings import *
from soccersimulator import AbstractStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
class fonceurStrategy(AbstractStrategy):
    def __init__(self):
        AbstractStrategy.__init__(self, "fonceur")
    def compute_strategy(self, state, id_team, id_player):
    	#balle = etat de la balle
        balle = state.ball
	#joueur = etat du joueur
	joueur = state.player_state(id_team, id_player)
	#distance_joueur_balle = c'est la distance entre le joueur et la balle
	distance_joueur_balle = balle.position.distance(joueur.position)
	#rayon_joueur_balle = rayon du joueur plus rayon de la balle
	rayon_joueur_balle = PLAYER_RADIUS + BALL_RADIUS
	#Il ne shoot que si la distance_joueur_balle est inferieure au rayon_joueur_balle
	if distance_joueur_balle < rayon_joueur_balle:
	     if id_team == 1:
		  action = SoccerAction(balle.position - joueur.position, Vector2D(x = GAME_WIDTH, y = GAME_HEIGHT/2.) - balle.position)
	     elif id_team == 2:
		  action = SoccerAction(balle.position - joueur.position, Vector2D(x = 0, y = GAME_HEIGHT/2.) - balle.position)
	     action_bis = action.copy()
	     action_ter = action + action_bis
	     return SoccerAction(action_ter.acceleration, action_ter.shoot)
	else:
	     return SoccerAction(balle.position - joueur.position)

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
