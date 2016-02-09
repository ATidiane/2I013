# -*-coding: utf8 -*
import soccersimulator
from soccersimulator.settings import *
from soccersimulator import SoccerAction, SoccerState, Vector2D, Player

#DEFINITION DES CONSTANTES

GOAL_SURFACE_WIDTH = GAME_WIDTH/10.
TIERS_TERRAIN = GAME_WIDTH - 50
MILIEU_TERRAIN = GAME_WIDTH/2.
QUART_TERRAIN = MILIEU_TERRAIN/2.

######################################################################################################
#                     Mystate: mes petites strategies ;)
######################################################################################################

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
    def vitesse_ball(self):
        """Vitesse de la balle"""
        return self.state.ball.vitesse

    @property
    def position_player(self):
        """Position du joueur"""
        return self.state.player_state(self.id_team,self.id_player).position

    @property
    def goal_un(self):
        """Position du goal1, c'est à dire à gauche"""
        return Vector2D(x = 0, y = GAME_HEIGHT/2.)

    @property
    def goal_deux_coin_bas(self):
        """Position du coin bas du goal1"""
        return Vector2D(x = GAME_WIDTH, y = GAME_HEIGHT/2. + 3.5)

    @property
    def goal_deux_coin_haut(self):
        """Position du coin haut du goal1"""
        return Vector2D(x = GAME_WIDTH, y = GAME_HEIGHT/2. - 3.5)

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
        """Rayon du joueur plus rayon nde la balle"""
        return PLAYER_RADIUS + BALL_RADIUS

    @property
    def fonce_ball(self):
        """Fonce vers la balle"""
        #if self.id_team == 2:
        #    print self.id_team,self.id_player,self.position_ball,self.position_player,SoccerAction(self.position_ball-self.position_player)
        return SoccerAction(self.position_ball - self.position_player)

    @property
    def shoot_ball(self):
        """Shoot la balle"""
        if self.distance_player_ball < self.rayon_player_ball:
            return SoccerAction((self.position_ball - self.position_player), (self.goal_deux - self.position_ball))
        else:
            return self.fonce_ball
    
    @property
    def shoot_ball_coin_bas(self):
        """Shoot la balle au coin bas, c'est à dire au premier poto du goal_deux"""
        return SoccerAction((self.position_ball - self.position_player), (self.goal_deux_coin_bas - self.position_ball))
    
    @property
    def shoot_ball_coin_haut(self):
        """Shoot la balle au coin haut, c'est à dire au deuxième poto du goal_deux"""
        return SoccerAction((self.position_ball - self.position_player), (self.goal_deux_coin_haut - self.position_ball))
    
    @property
    def shoot_ball_smart(self):
        """Choisi quand shooter au premier ou au deuxième poto ou encore au milieu du goal"""
        if self.distance_player_ball < self.rayon_player_ball:
            if (self.position_ball.y <= GAME_HEIGHT - 46) and (self.position_ball.x >= MILIEU_TERRAIN - 5):
                return self.shoot_ball_coin_bas
            elif (self.position_ball >= GAME_HEIGHT - 44) and (self.position_ball.x >= MILIEU_TERRAIN - 5):
                return self.shoot_ball_coin_haut
            else:
                return SoccerAction((self.position_ball - self.position_player), (self.goal_deux - self.position_ball))
        else:
            return self.fonce_ball

    @property
    def shoot_ball_g(self):
        """Shoot la balle vers la gauche avec un angle de 45 dégré"""
        if self.distance_player_ball < self.rayon_player_ball:
            return SoccerAction((self.position_ball - self.position_player), Vector2D(x = 105, y = 80) - self.position_ball)
        

    @property 
    def shoot_ball_d(self):
        """Shoot la balle vers la droite avec un angle de 45 dégré"""
        if self.distance_player_ball < self.rayon_player_ball:
            return SoccerAction((self.position_ball - self.position_player), Vector2D(x = 105, y = 10))

    @property
    def defense(self):
        """Defenseur"""
        if (self.position_ball.x <= MILIEU_TERRAIN + 5):
                return self.shoot_ball_smart
        elif (self.position_ball - self.position_player >= 70) and (self.position_ball.x >= MILIEU_TERRAIN + 15):
            return SoccerAction(Vector2D(x = self.position_ball.x - 50, y = self.position_ball.y) - self.position_player)
        elif (self.position_ball - self.position_player <= 20):
            return self.shoot_ball
        else:
            return SoccerAction(Vector2D(x = GAME_WIDTH/6., y = GAME_HEIGHT/2.) - self.position_player)

    
    @property
    def keeper_shoot_g(self):
        """Shoot vers la gauche du milieu du terrain"""
        return SoccerAction((self.position_ball - self.position_player), Vector2D(x = MILIEU_TERRAIN - 5, y = GAME_HEIGHT - 5) - self.position_ball)

    @property
    def keeper_shoot_d(self):
        """Shoot vers la droite du milieu du terrain"""
        return SoccerAction((self.position_ball - self.position_player), Vector2D(x = MILIEU_TERRAIN - 5, y = 5) - self.position_ball)

    @property
    def position_goalkeeper(self):
        """Position du gardien"""
        if (self.distance_player_ball <= GOAL_SURFACE_WIDTH):
            if (self.position_ball.y >= 46):
                return self.keeper_shoot_g
            else:
                return self.keeper_shoot_d
        elif (self.position_ball.y <= GAME_HEIGHT - 49) and (self.position_ball.x >= GAME_WIDTH/12.):
            return SoccerAction((self.goal_un - 3) - self.position_player) 
        elif (self.position_ball.y >= GAME_HEIGHT - 41) and (self.position_ball.x >= GAME_WIDTH/11.):
            return SoccerAction((self.goal_un + 3) - self.position_player)
        elif (self.position_ball.x >= TIERS_TERRAIN):
            return SoccerAction(Vector2D(x = GAME_WIDTH/11., y = GAME_HEIGHT/2.) - self.position_player)
        return SoccerAction(Vector2D(x = 1, y = GAME_HEIGHT/2.) - self.position_player)



######################################################################################################
#                         Fin de mes petites strategies
######################################################################################################

def fonceur(mystate):
    return mystate.fonce_ball

def fonceur_shooteur(mystate):
    return mystate.shoot_ball

def gardien(mystate):
    return mystate.position_goalkeeper

def defenseur(mystate):
    return mystate.defense

def shooteur_ball_smart(mystate):
    return mystate.shoot_ball_smart

######################################################################################################
#          Miroir: ps un gros problème
######################################################################################################

def miroir_p(p):
    return Vector2D(GAME_WIDTH - p.x, p.y)

def miroir_v(v):
    return Vector2D(-v.x, v.y)

def miroir_socac(action):
    return SoccerAction(miroir_v(action.acceleration), miroir_v(action.shoot))

def miroir_state(s):
    res = s.copy()
    res.ball.position = miroir_p(s.ball.position)
    res.ball.vitesse  = miroir_v(s.ball.vitesse)
    for (id_team, id_player) in s.players:
        res.player_state(id_team, id_player).position = miroir_p(s.player_state(id_team, id_player).position)
        res.player_state(id_team, id_player).vitesse = miroir_v(s.player_state(id_team, id_player).vitesse)
    return res

######################################################################################################
#          Fin de ce beau miroir
######################################################################################################







######################################################################################################
#                                         Brouillon
######################################################################################################

"""    @property
    def shoot_ball(self):
        Shoot la balle vers la droite
        if self.distance_player_ball < self.rayon_player_ball:
            if self.id_team == 1:
                return SoccerAction((self.self.state.ball.position - self.position_player), (self.goal_deux - self.self.state.ball.position))
            elif self.id_team == 2:
                return SoccerAction((self.self.state.ball.position - self.position_player), (self.goal_un - self.self.state.ball.position))
        else:
            return self.fonce_ball"""


######################################################################################################
#                                      Fin du Brouillon
######################################################################################################
