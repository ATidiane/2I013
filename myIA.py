from soccersimulator import SoccerTeam, Player
from coordination import *
from decisiontree import gen_features, DTreeStrategy
import cPickle

#######################################
# strat IA
#######################################

tree = cPickle.load(file("/users/nfs/Etu4/3502264/Documents/2I013/mon_repo_git/monfichier.pkl"))
dic = {"fonceur_shooteur":fonceur_shooteur, "shooteur_ball_smart":buteur, "run_ball_avant_normalize":runv_goal, "run_ball_arriere_normalize":runv_goal_arr, "dribleur":dribleur}
treeStrat = DTreeStrategy(tree,dic,gen_features)
