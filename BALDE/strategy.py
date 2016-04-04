# -*-coding: utf8 -*
import soccersimulator
from soccersimulator.settings import *
from soccersimulator import SoccerAction, SoccerState, Vector2D, Player
from math import pi
from random import *

#DEFINITION DES CONSTANTES

GOAL_SURFACE_WIDTH = GAME_WIDTH/9.
THIRD_WIDTH = GAME_WIDTH - 50
MEDIUM_WIDTH = GAME_WIDTH/2.
QUARTER_WIDTH = MEDIUM_WIDTH/2.
THREE_QUARTER_WIDTH = MEDIUM_WIDTH + QUARTER_WIDTH
MEDIUM_HEIGHT = GAME_HEIGHT/2.
QUARTER_HEIGHT = MEDIUM_HEIGHT/2.
THREE_QUARTER_HEIGHT = MEDIUM_HEIGHT + QUARTER_HEIGHT

######################################################################################################
#                     Mystate: mes petites strategies ;)
######################################################################################################

class Mystate:
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player =id_player

    @property
    def goal_un(self):
        """Position du goal1, c'est à dire à gauche"""
        return Vector2D(x = 0, y = MEDIUM_HEIGHT)

    @property
    def goal_deux(self):
        """Position du goal2, c'est à dire à droite"""
        return Vector2D(x = GAME_WIDTH, y = MEDIUM_HEIGHT)
    
    @property
    def vitesse_player(self):
        """Vitesse de la balle"""
        return self.state.player_state(self.id_team, self.id_player).vitesse

    @property
    def position_ball(self):
        """Position de la balle"""
        return self.state.ball.position

    @property
    def position_player(self):
        """Position du joueur"""
        return self.state.player_state(self.id_team, self.id_player).position

    @property
    def fonce_ball(self):
        """Fonce vers la balle"""
        return SoccerAction(self.position_ball - self.position_player)

    @property
    def shoot_ball(self):
        """Shoot la balle"""
        if self.distance_player_ball < self.rayon_player_ball:
            if self.position_ball.x >= THREE_QUARTER_WIDTH:
                return SoccerAction(Vector2D(), (self.goal_deux - self.position_ball).norm_max(4))
            else:
                return SoccerAction(Vector2D(), (self.goal_deux - self.position_ball))
        return self.fonce_ball

    @property
    def rayon_player_ball(self):
        """Rayon du joueur plus rayon nde la balle"""
        return PLAYER_RADIUS + BALL_RADIUS

    @property
    def distance_player_ball(self):
        """Distance entre le joueur et la balle	"""
        return self.position_ball.distance(self.position_player)
    
    @property
    def myguys_position(self):
        """Position de tous mes joueurs"""
        lalya = []
        if self.id_team == 1:
            if self.state.nb_players(1) == 1:
                lalya.append(self.state.player_state(1, 0).position)
            elif self.state.nb_players(1) == 2:
                for i in range(2):
                    pos = self.state.player_state(1, i).position
                    lalya.append(pos)
            elif self.state.nb_players(1) == 4:
                for i in range(4):
                    pos = self.state.player_state(1, i).position
                    lalya.append(pos)
        elif self.id_team == 2:
            if self.state.nb_players(2) == 1:
                lalya.append(self.state.player_state(2, 0).position)
            elif self.state.nb_players(2) == 2:
                for i in range(2):
                    pos = self.state.player_state(2, i).position
                    lalya.append(pos)
            elif self.state.nb_players(2) == 4:
                for i in range(4):
                    pos = self.state.player_state(2, i).position
                    lalya.append(pos)
        #Retourne une liste de toutes les positions de mes joueurs, quelque soit la team ou le nombre de joueurs.
        return lalya

    @property
    def adv_position(self):
        """Position de tous mes joueurs"""
        lalya = []
        if self.id_team == 1:
            #state.nb_players prend en paramètre le numéro de la team, donc 1 ou 2
            #et retourne le nombre de joueurs.
            if self.state.nb_players(2) == 1:
                lalya.append(self.state.player_state(2, 0).position)
            elif self.state.nb_players(2) == 2:
                #range(2) si le nombre de joueurs de la team adverse est 2, à noter que self.id_player commence à 0.
                for i in range(2):
                    pos = self.state.player_state(2, i).position
                    #Et on ajoute la position de chancun des joueurs de la team 2(adverse) à la liste.
                    lalya.append(pos)
            elif self.state.nb_players(2) == 4: 
                #range(4) si le nombre de joueurs de la team adverse est 4, à noter que self.id_player commence à 0.
                for i in range(4):
                    pos = self.state.player_state(2, i).position
                    lalya.append(pos)
        elif self.id_team == 2:
            if self.state.nb_players(1) == 1:
                lalya.append(self.state.player_state(1, 0).position)
            elif self.state.nb_players(1) == 2:
                for i in range(2):
                    pos = self.state.player_state(1, i).position
                    lalya.append(pos)
            elif self.state.nb_players(1) == 4:
                for i in range(4):
                    pos = self.state.player_state(1, i).position
                    lalya.append(pos)
        #Retourne une liste de toutes les positions de mes joueurs, quelque soit la team ou le nombre de joueurs.
        return lalya
    def proche(self, rang=1):
        """Le joueur le plus proche en fonction du rang ;)"""
        dist_pos = {}
        lalya = []
        monrg = self.myguys_position
        #Pour ajouter la distance et la position de chaque joueur sauf lui même
        #Par exmple, le dictionnaire ressemblera à ça:
        #{18.0: Vector2D'>: (53.637907,58.162304), 14.0: Vector2D'>: (57.593337,59.041951)}
        for i in monrg:
            #Pour eviter de calculer la distance de moi à moi
            if i != self.position_player:
                d = self.position_player.distance(i)
                dist_pos[round(d,2)] = i
        #Pour ajouter les clés en l'occurence les distances dans une liste, afin de recuperer
        #la position du joueur qui est à cette distance moi.
        for i in dist_pos.keys():
            lalya.append(i)
        #On trie la liste pour avoir le plus proche au plus loin
        lalya.sort()
        #Après le trie, la liste ressemblera à: [14.0, 18.0]
        #Pour recuperer la position qui se trouve à une distance(clé)
        pos = dist_pos.get(lalya[rang-1])
        #Retourne la position
        return pos

        
    def proche_ball(self, qui=1, rang=1):
        """Retourne la position du joueur le plus proche de la ball, selon le rang
        Si qui == 1 alors je veux la position de MON joueur, si qui == 2 alors,
        renvoie la position du joueur adverse, si qui == "autre chose", alors exit"""
        dist_pos = {}
        lalya = []
        #Si qui == 1 alors je veux appliquer la fonction sur mes joueurs
        if qui == 1:
            monrg = self.myguys_position
        #Si qui == 2 alors je veux appliquer la fonction sur les joueurs adverses
        elif qui == 2:
            monrg = self.adv_position
        #Sinon si qui == "autre chose" exit()
        else:
            exit()
        for i in monrg:
            d = i.distance(self.position_ball)
            dist_pos[d] = i
        for i in dist_pos.keys():
            lalya.append(i)
        lalya.sort()
        pos = dist_pos.get(lalya[rang-1])
        return pos

    @property
    def PasseC(self):
        """Le joueur passe à l'équipier le mieux placé pour recevoir le ballon
        C'est à dire dans mon cas, le plus loin d'un joueur adverse, à part le gardien"""
        dist_pos = {}
        lalya = []
        tmpdic = {}
        tmplist = []
        monrg = self.myguys_position
        advrg = self.adv_position
        for i in monrg:
            for j in advrg:
                d = i.distance(j)
                tmpdic[d] = j
            for i in tmpdic.keys():
                tmplist.append(i)
            tmplist.sort()
            dist_pos[tmplist[1]] = i
        for i in dist_pos.keys():
            lalya.append(i)
        lalya.sort()
        pos = dist_pos.get(lalya[-1])
        return pos

    @property
    def passe_proche(self):
        vecteur_vitesse = self.vitesse_player
        norm = vecteur_vitesse.normalize()
        if norm < 0.01:
            return SoccerAction(Vector2D(), (self.passeC - self.position_ball))
        elif self.position_player == self.proche_ball():
            return self.fonce_ball
        else:
            return SoccerAction()
    
    def shoot(self, pos):
        vecteur_vitesse = self.vitesse_player
        norm = vecteur_vitesse.normalize()
        if norm < 0.01:
            return SoccerAction(Vector2D(), (pos - self.position_ball))
        return self.fonce_ball
        
    @property
    def passe_second_j(self):
        """Passe la ball au joueur le plus proche"""
        monrg = self.myguys_position
        for pos in monrg:
            if pos != self.position_player:
                self.shoot(pos)
                if (self.position_player == self.proche_ball()):
                    return self.fonce_ball + self.shoot(pos)
                elif (self.position_player != self.proche_ball()):
                    if self.position_ball.y > MEDIUM_HEIGHT:
                        return SoccerAction(Vector2D(self.position_ball.x + 40, self.position_ball.y + 10) - self.position_player)
                    elif self.position_ball.y < MEDIUM_HEIGHT:
                        return SoccerAction(Vector2D(self.position_ball.x + 40, self.position_ball.y - 10) - self.position_player)
                else:
                    return SoccerAction()
    
        



######################################################################################################
#Fin des strategies
######################################################################################################
def passeurC(mystate):
    return mystate.PasseC

def fonceur_shooteur(mystate):
    return mystate.shoot_ball

def passe_equipier(mystate):
    return mystate.passe_second_j

def passe_team4(mystate):
    return mystate.passe_proche
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
