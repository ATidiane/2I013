# -*-coding: utf8 -*
import soccersimulator
from soccersimulator.settings import *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament

#DEFINITION DES CONSTANTES
GOAL_SURFACE_WIDTH = GAME_WIDTH/13.

def position_ball(state):
    """Position de la balle"""
    return state.ball.position

def position_player(state, id_team, id_player):
    """Position du joueur"""
    return state.player_state(id_team, id_player).position

def fonce_ball(state, id_team, id_player):
    """Fonce vers la balle"""
    return SoccerAction(position_ball(state) - position_player(state, id_team, id_player))

def distance_player_ball(state, id_team, id_player):
    """Distance entre le joueur et la balle	"""
    return position_ball(state).distance(position_player(state, id_team, id_player))

def rayon_player_ball():
    """Rayon du joueur plus rayon de la balle"""
    return PLAYER_RADIUS + BALL_RADIUS 
	
def shoot_ball_team1(state, id_team, id_player):
    """Shoot la balle vers la droite"""
    if distance_player_ball(state, id_team, id_player) < rayon_player_ball():
	return SoccerAction(position_ball(state) - position_player(state, id_team, id_player), Vector2D(x = GAME_WIDTH, y = GAME_HEIGHT/2.) - position_ball(state))
    else:
        return fonce_ball(state, id_team, id_player)

def shoot_ball_team2(state, id_team, id_player):
    """Shoot la balle vers la gauche"""
    if distance_player_ball(state, id_team, id_player) < rayon_player_ball():
	return SoccerAction(position_ball(state) - position_player(state, id_team, id_player), Vector2D(x = 0, y = GAME_HEIGHT/2.) - position_ball(state))
    else:
        return fonce_ball(state, id_team, id_player)

def position_goalkeeper(state, id_team, id_player):
    """Position du gardien"""
    if distance_player_ball(state, id_team, id_player) < GOAL_SURFACE_WIDTH:
        return shoot_ball_team1(state, id_team, id_player)
    elif position_ball(state).y <= GAME_HEIGHT - 50 and position_ball(state).x >= GAME_WIDTH/11.:
        return SoccerAction(Vector2D(x = 1, y = (GAME_HEIGHT/2.) - 2) -
        position_player(state, id_team, id_player)) 
    elif position_ball(state).y >= GAME_HEIGHT - 40 and position_ball(state).x >= GAME_WIDTH/11.:
        return SoccerAction(Vector2D(x = 1, y = (GAME_HEIGHT/2.) + 2) -
        position_player(state, id_team, id_player))
    else:
        return SoccerAction(Vector2D(x = 1, y = GAME_HEIGHT/2.) - position_player(state, id_team, id_player))

