# -*-coding: utf8 -*
import soccersimulator
from soccersimulator.settings import *
from soccersimulator import SoccerAction, Vector2D, Player

#DEFINITION DES CONSTANTES
GOAL_SURFACE_WIDTH = GAME_WIDTH/13.

class Mystate:
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player =id_player

    @property
    def position_ball(self):
        """Position de la balle"""
        return self.state.ball.position

    @property
    def position_player(self):
        """Position du joueur"""
        return self.state.player_state(self.id_team,self.id_player).position

    @property
    def goal_un(self):
        """Position du goal1, c'est à dire à gauche"""
        return Vector2D(x = 0, y = GAME_HEIGHT/2.)

    @property
    def goal_deux(self):
        """Position du goal2, c'est à dire à droite"""
        return Vector2D(x = GAME_WIDTH, y = GAME_HEIGHT/2.)

    @property
    def distance_player_ball(self):
        """Distance entre le joueur et la balle	"""
        return self.position_ball.distance(self.position_player)

    @property
    def rayon_player_ball(self):
        """Rayon du joueur plus rayon de la balle"""
        return PLAYER_RADIUS + BALL_RADIUS

    @property
    def fonce_ball(self):
        """Fonce vers la balle"""
        return SoccerAction(self.position_ball - self.position_player)

    @property
    def shoot_ball(self):
        """Shoot la balle"""
        if self.distance_player_ball < self.rayon_player_ball:
            return SoccerAction((self.position_ball - self.position_player), (self.goal_deux - self.position_ball))
        else:
            return self.fonce_ball

#    @property
#    def shoot_ball(self):
#        """Shoot la balle vers la droite"""
#        if self.distance_player_ball < self.rayon_player_ball:
#            if self.id_team == 1:
#                return SoccerAction((self.position_ball - self.position_player), (self.goal_deux - self.position_ball))
#            elif self.id_team == 2:
#                return SoccerAction((self.position_ball - self.position_player), (self.goal_un - self.position_ball))
#        else:
#            return self.fonce_ball

    @property
    def position_goalkeeper(self):
        """Position du gardien"""
        if self.distance_player_ball < GOAL_SURFACE_WIDTH:
            return self.shoot_ball
        elif (self.position_ball.y <= GAME_HEIGHT - 50) and (self.position_ball.x >= GAME_WIDTH/11.):
            return SoccerAction((self.goal_un - 2) - self.position_player) 
        elif (self.position_ball.y >= GAME_HEIGHT - 40) and (self.position_ball.x >= GAME_WIDTH/11.):
            return SoccerAction((self.goal_un + 2) - self.position_player)
        elif (self.position_ball.x >= GAME_WIDTH - 50):
            return SoccerAction(Vector2D(x = GAME_WIDTH/11., y = GAME_HEIGHT/2.) - self.position_player)
        else:
            return SoccerAction(Vector2D(x = 1, y = GAME_HEIGHT/2.) - self.position_player)
        

def fonceur(mystate):
    return mystate.fonce_ball

def fonceur_shooteur(mystate):
    return mystate.shoot_ball

def gardien(mystate):
    return mystate.position_goalkeeper
