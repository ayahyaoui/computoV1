# =========================================================================== #
# ____________________  |Importation des lib/packages|   ____________________ #
# =========================================================================== #
import numpy.random as rand
from string import ascii_letters, digits

AUTHORIZED_OPERATORS = ['+', '-', '*', '/', '^']
parenthesis = ['(', ')']
AUTHORIZED_DIGITS = list(digits)
AUTHORIZED_VAR = list(ascii_letters)
MAX_DIGITS = 10
# =========================================================================== #
# _____________________    |Definition des fonctions|   _____________________ #
# =========================================================================== #
def wrap_construct_nb():
	n_digits = rand.randint(1 , MAX_DIGITS , 1)
	neg = rand.randint(2)
	floating_pt = rand.randint(MAX_DIGITS)
	
	n = construct_nb(n_digits, neg, floating_pt)
	
	return n


def construct_nb(n_digits, neg, floating_pt):
	res = ""
	print(f"     -neg = {neg}  --  n_digits = {n_digits}  --  floating_pt = {floating_pt}")
	if neg:
		res += '-'
	dgts = rand.randint(9, size=n_digits)
	dgts = list(dgts)
	dgts = [str(elem) for elem in dgts]
	l = 0
	for dgt in dgts:
		if (l == floating_pt):
			res += '.'
		res += dgt
		l += 1
	return res


def draw_operator():
	i = rand.randint(0,len(AUTHORIZED_OPERATORS))
	return AUTHORIZED_OPERATORS[i]



# =========================================================================== #
# _______________________________    |MAIN|   _______________________________ #
# =========================================================================== #
if __name__ == "__main__":
	print(AUTHORIZED_OPERATORS)
	print(AUTHORIZED_DIGITS)
	print(AUTHORIZED_VAR)

	for i in range(20):
		nb = wrap_construct_nb()
		#print(f"tirage #{i}:  ", f"|{nb}|", f"  (type = {type(nb)})")
	
	# Need to change the approach, take a look to: https://stackoverflow.com/questions/6881170/is-there-a-way-to-autogenerate-valid-arithmetic-expressions


