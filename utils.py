

from myast import *
global VERBOSE
VERBOSE  = 4

dict_message = {"PB":"...",
				"ERROR":"...",
				"BONUS":"...",
				"MAIN":""}

	
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	NOC = "\033[0m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	BLACK = "\033[1;30m"
	RED = "\033[1;31m"
	GREEN = "\033[1;32m"
	YELLOW = "\033[1;33m"
	BLUE = "\033[1;34m"
	VIOLET = "\033[1;35m"
	CYAN = "\033[1;36m"
	WHITE = "\033[1;37m"


def affichage(*argv):
	for key in dict_message:
		found = False
		if key == argv[0]:
			print(dict_message[0], "in ",  *argv[1:])
			found = True
	if not found:
		print(*argv[2:])

	
"""
	Compte le nombre d Monome non nul
"""
def count_Monome(list_token):
	count = 0
	for token in list_token:
		if isinstance(token, MyMonomial):
			count += 1
	return count

"""
	Pour une liste d Monome renvoie une liste addition en NPI
	(notation polonaise inversee) 
	exemple  [Xˆ2, 42] -> [Xˆ2, 42, +]
"""
def fill_addition_NPI(list_token):
	new_result = [list_token[0]]
	for elem in list_token[1:]:
		new_result.append(elem)
		new_result.append(Token('+'))
		new_result[-1].group = new_result[0].group
	list_token = new_result
	return new_result


"""
	Pour une liste de Monome et de '+' renvoie une liste addition en NPI simplifier
	(notation polonaise inversee) 
	exemple  [Xˆ2, 21, +, 21, +] -> [Xˆ2, 42, +]

"""
def simplification_addition(list_token):
	if VERBOSE > 3:
		print(f"     {bcolors.BLUE}Simplifions:{bcolors.ENDC} ", list_token)
	rest_equation = []
	dict_power = {}
	for token in list_token:
		if isinstance(token, MyMonomial):
			if token.exposant in dict_power:
				dict_power[token.exposant] += token.coefficient
			else:
				dict_power[token.exposant] = token.coefficient
		elif token.type_token != dct_tokens['+']:
			# catch Error
			affichage("", "", "Probleme signe non attendu ici", first_operand)
	result = [MyMonomial(value, key) for key, value in dict_power.items()]
	result = fill_addition_NPI(result)
	if VERBOSE > 3:
		print(f"     {bcolors.FAIL}", list_token, f"{bcolors.ENDC} ={bcolors.OKGREEN}", result, f"{bcolors.ENDC}\n")
	return result     