# =========================================================================== #
# ____________________  |Importation des lib/packages|   ____________________ #
# =========================================================================== #

# =========================================================================== #
# _____________________   |Definition des constantes|   _____________________ #
# =========================================================================== #

dct_tokens = {"(" : 1,
			  ")" : 2,
			  "+" : 3,
			  "-" : 4,
			  "/" : 5,
			  "*" : 6,
			  "=" : 7,
			  "ˆ" : 8,
			  '^' : 8,
			  "UNKNOWN": 9,
			  "VARIABLE": 10,
			  "NUMBER": 11}

dict_operator_priority = {
			  "+" : 1,
			  "-" : 1,
			  "/" : 2,
			  "*" : 2,
			  "ˆ" : 3,
			  '^' : 3,
			  "=" : 4}
global VERBOSE
VERBOSE  = 4
# =========================================================================== #
# __________________   |Definition des classes pour AST|   __________________ #
# =========================================================================== #

class Token():
	def __init__(self, t):
		self.value = t
		self.group = 1
		if t in list("()+-*/=^ˆ"):
			self.type_token = dct_tokens[t]
		elif t.isdigit():
			self.type_token = dct_tokens["NUMBER"]
			self.value = int(t)
		elif isfloat(t):
			self.type_token = dct_tokens["NUMBER"]
			self.value = float(t)
		elif t.isalpha():
			self.type_token = dct_tokens["VARIABLE"]
			self.value = t
		else:
			self.type_token = dct_tokens["UNKNOWN"]
			self.value = t


	def __repr__(self):
		if self.type_token <= 2:
			tk_type = "parenthesis"
		elif self.type_token <= 8:
			tk_type = "operator"
		elif self.type_token == 9:
			tk_type = "?"
		elif self.type_token == 10:
			tk_type = "variable"
		elif self.type_token == 11:
			tk_type = "number"
		else:
			tk_type = "ERROR"
		return str(self.value)
		#return "Tkn{" + str(self.value) + ":" + tk_type + "}"


class MyMonomial(Token):
	def __init__(self, coefficient, exposant):
		name = '1' # A CHANGER (mettre en paramettre)
		Token.__init__(self, name) 
		self.coefficient = coefficient
		self.exposant = exposant


	def __repr__(self):
		s_coef, s_var, s_exp = '', '', ''
		if abs(self.exposant) >= 1:
			s_var = 'X'
		if self.exposant > 1 or self.exposant <= -1:
			s_exp = '^' + str(self.exposant)
		if abs(self.coefficient) != 1 or self.exposant == 0 :
			s_coef = str(self.coefficient)
		elif self.coefficient == -1:
			s_coef = '-'
		if self.coefficient == 0:
			return '0'
		return '' + s_coef + s_var + s_exp


	def multiply_MyMonomial(self, monome):
		self.coefficient *= monome.coefficient
		self.exposant += monome.exposant


	def divide_MyMonomial(self, monome):
		if monome.coefficient == 0:
			raise ZeroDivisionError("Division by zero")
		self.coefficient /= monome.coefficient
		self.exposant -= monome.exposant


	def add_MyMonomial(self, monome):
		if self.exposant != monome.exposant:
			raise Exception
		self.coefficient += monome.coefficient


	def soustract_MyMonomial(self, monome):
		if self.exposant != monome.exposant:
			raise Exception
		self.coefficient -= monome.coefficient


	def power_MyMonomial(self, monome):
		if monome.exposant != 0:
			raise Exception("Monome in exposant")
		self.exposant *= monome.coefficient
		self.coefficient **= monome.coefficient


def isfloat(s:str) -> bool:
	""" Functions to determine if the parameter s can be represented as a float
	Parameters:
	-----------
		* s [str]: string which could be or not a float.
	Return:
	-------
		* True: s can be represented as a float.
		* False: s cannot be represented as a float.
	"""
	float_c = list(".0123456789")
	if not all([c in float_c for c in s]):
		return False
	return True


def is_operator(token:Token) -> bool:
	""" Functions to determine if the token is an operator type.
	Parameters:
	-----------
		* token [Token instance]: a Token instance.
	Return:
	-------
		* True: token is an operator.
		* False: token is not an operator.
	"""
	if token.value in list("+-*/ˆ^"):
		return True
	return False