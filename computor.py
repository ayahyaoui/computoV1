# =========================================================================== #
# ____________________  |Importation des lib/packages|   ____________________ #
# =========================================================================== #
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import sys

from parsing import parser, check_validity

#from myast import *
#import myast 
from myast import MyMonomial, VERBOSE
from conversion import convert_expression
from developpement import developpement
from utils import  *
from polynomial import Polynomial
from polynomial_bonus import PolynomialBonus

# =========================================================================== #
# ___________________________    |FUNCTIONS|     ____________________________ #
# =========================================================================== #
def check_polynom(exprs:list):
	""" Function checks the power of the monomes within the expressions.
	An accepted polynomial expression in computer-v1 is a polynom with monomes
	which do not exceed the power 2.
	"""
	pass


def process_polynom(list_monoms, b_bonus=False):
	param = [0] * (list_monoms[0].exposant+1)
	for elem in list_monoms:
		param[elem.exposant] = elem.coefficient
	param = param[::-1]
	#if list_monoms[0].exposant > 3:
	#	print("impossible le polynome est de degres", list_monoms[0].exposant)
	#	return False
	if b_bonus:
		polynom = PolynomialBonus(param)
	else:
		polynom = Polynomial(param)
	return polynom
	

def process(list_test, b_bonus=False):
	"""
	... Docstring ...
	"""
	#try:
	if VERBOSE > 1:
		affichage("", "", f"{bcolors.OKBLUE}liste avant conversion :{bcolors.ENDC}", list_test)
	list_converti = convert_expression(list_test)
	if VERBOSE > 1:
		affichage("", "", f"{bcolors.OKBLUE}liste apres conversion :{bcolors.ENDC}", list_converti)
	if VERBOSE > 2:			
		affichage("", "", f"{bcolors.OKBLUE}DEVELOPPEMENT:\n\n{bcolors.ENDC}", list_converti)
	list_developper = developpement(list_converti)
	if VERBOSE > 1:
		affichage("", "", f"{bcolors.OKBLUE}\nliste apres developpement:{bcolors.ENDC}", list_developper)
	list_expression = [elem for elem in list_developper if isinstance(elem, MyMonomial)\
			and (elem.coefficient != 0 or elem.exposant == 0)]
	#if list_expression == []:
	#	list_expression = [MyMonomial(0,0)]
	list_expression = sorted(list_expression, key=lambda val: val.exposant)[::-1]
	if VERBOSE > 0:
		affichage("", "", f"{bcolors.OKBLUE}\nForme developper :{bcolors.ENDC}",  ' + '.join(map(str,list_expression)))
#except:
#	print(f"{bcolors.RED}CATCH ERROR: {bcolors.ENDC}",e)
#	print(f"{bcolors.OKBLUE}AU REVOIR{bcolors.ENDC}")
#	exit()
	polynom = process_polynom(list_expression, b_bonus)
	return polynom		
#except Exception as e:
#	print(e)



# =========================================================================== #
# ______________________________    |MAIN|     ______________________________ #
# =========================================================================== #
if __name__ == "__main__":
	args = sys.argv
	
	# --- Parsing --- #
	if len(args) == 1:
		print("No argument.")
		sys.exit()
	if args[1] == "--bonus=on":
		b_bonus = True
		args = args[1:]
	else:
		b_bonus = False
	exprs = parser(args[1:])
	if exprs is None:
		sys.exit()
	
	for expr in exprs:
		# --- Processing --- #
		polynom = process(expr, b_bonus)

		# --- Verbose, information on the polynomial --- #
		polynom.summarize()
