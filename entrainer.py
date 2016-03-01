""" Permet de jouer et d'entrainer une strategie
    * changer les strategies ajoutees
    * utilisation : python entrainer prefix_fichier_exemple
    par defaut ajoute au fichier d'exemples sil existe deja
    (extension : .exp pour le fichier exemple)
"""

from soccersimulator import SoccerMatch, show, SoccerTeam,Player,KeyboardStrategy
from decisiontree import DTreeStrategy, gen_features
import cPickle
from coordination import *
from team import *
import sys


### Entrainer un arbre

prefix = "tree"
if len(sys.argv)>1:
    prefix = sys.argv[1]
strat_key = KeyboardStrategy(fn="monfichier.exp") #fn veut dire filename
strat_key.add("f", fonceur_shooteur)
strat_key.add("b", buteur)
strat_key.add("r", runv_goal)
strat_key.add("t", runv_goal_arr)
strat_key.add("d", dribleur)
t1j1 = Player("t1j1", strat_key)
dogomet1 = SoccerTeam("dogomet1", [t1j1])
match_dogomet1 = SoccerMatch(dogomet1, lalya1)
    
if __name__=="__main__":
    show(match_dogomet1)
