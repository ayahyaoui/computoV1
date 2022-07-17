# =========================================================================== #
# ____________________  |Importation des lib/packages|   ____________________ #
# =========================================================================== #
from utils import bcolors as color

# =========================================================================== #
# _____________________   |Definition des constantes|   _____________________ #
# =========================================================================== #
prec = 1e-7

# =========================================================================== #
# ______________________   |Definition des classes |   ______________________ #
# =========================================================================== #
class Polynomial():

	def __init__(self, list_coeff):
		"""Creates the polynomial instance based on the list of coefficients.
		Remark:
		-------
			Coefficients in the list are ordered from the coef of the highest
			MyMonomial degree to the MyMonomial of degree 0 (i.e. scalar constant)
		Example:
		--------
			polynomial expr: a.Xˆ3 + b.X ˆ2 + c.X + d => [a, b, c, d]
		Note:
		-----
			There is no gap in coefficient, meaning that a polynomial expr
			without a specific MyMonomial of degree i has still its coefficient
			in list_coeff but it is set to zero.
			a.X^3 + b => [a, 0, 0, b]
		"""
		self.coefs = list_coeff
		while len(self.coefs) > 0 and self.coefs[0] == 0:
			self.coefs = self.coefs[1:]
		self.degree = len(self.coefs) - 1

	def _zero_degree_resolution_(self):
		"""Calculates the roots of polynomial of degree 0.
		Return:
		-------
			* r [floats]: roots of the polynomial.
		"""
		if self.degree == 0:
			a = self.coefs[0]
			if a == 0:
				r = 0
			if a != 0:
				r = None
			return [r]
		else:
			s_raise = "Polynomial is not of 0th degree."

	
	def _first_degree_resolution_(self):
		"""Calculates the roots of polynomial of degree 1.
		Return:
		-------
			* r [floats]: roots of the polynomial.
		"""
		if self.degree == 1:
			a = self.coefs[0]
			b = self.coefs[1]
			r = -b / a
			return [r]
		else:
			s_raise = "Polynomial is not of 1st degree."
			raise Exception(s_raise)

	def discriminant(self) -> float:
		""" Calculates the discriminant of the polynomial.
		Parameters:
		-----------
			* self [SecondOrderPolynomial class object]: ...

		Return:
		-------
			delta [float]: value of the discriminant constituted of tkn_m1/2/3.
		"""
		if self.degree == 2:
			a = self.coefs[0]
			b = self.coefs[1]
			c = self.coefs[2]
			delta = b * b - 4 * a * c
			return delta
		elif self.degree == 3:
			a = self.coefs[0]
			b = self.coefs[1]
			c = self.coefs[2]
			d = self.coefs[3]
			delta = 18 * a * b * c * d - 4 * power(b, 3) * d + power(b * c, 2) \
				- 4 * a * power(c, 3) - 27 * power(a * d, 2)
			return delta
		else:
			s_raise = "discriminant implementation for 2nd degree polynomial."
			raise Exception(s_raise)


	def _second_degree_resolution_(self):
		"""Calculates the roots of polynomial of degree 2.
		Return:
		-------
			* r1, r2 / r [floats/complexes]: roots of the polynomial.
		"""
		if self.degree == 2:
			delta = self.discriminant()
			b = self.coefs[1]
			a = self.coefs[0]
			if delta > 0:
				r1 = 0.5 * (-b - babylonian_sqrt(delta)) / a
				r2 = 0.5 * (-b + babylonian_sqrt(delta)) / a
				return [r1, r2]
			elif delta == 0:
				return [(- 0.5 * b / a)]
			else:
				real = - 0.5 * b / a
				imaginary = 0.5 * babylonian_sqrt(-delta) / a
				r1 = complex(real, -imaginary)
				r2 = complex(real, imaginary)
				return [r1, r2]
		else:
			s_raise = "Polynomial is not of 2nd degree."
			raise Exception(s_raise)


	def _third_degree_resolution_(self):
		""" Calculates the roots of polynomial of degree 3.
		The function is here for the completeness of the class and avoid
		the redefinition of the some methods in the class PolynomialBonus.
		"""
		# reference: https://fr.wikiversity.org/wiki/Équation_du_troisième_degré/Méthode_de_Cardan
		if self.degree == 3:
			msg = "3rd degree resolution is a project's bonus. " \
				+ "Use instance of class PolynomialBonus to have access to " \
				+ "to the resolution of 3rd degree polynomial."
			print(color.YELLOW + msg + color.NOC)
			return []
		else:
			print("Polynomial is not of 3rd degree.")


	def polynomial_roots(self):
		"""Calculates the roots of the polynomial.
		Return:
		-------
			delta [float]: value of the discriminant constituted of tkn_m1/2/3.
		"""
		roots = None
		if self.degree == 0:
			roots = self._zero_degree_resolution_()
		if self.degree == 1:
			roots = self._first_degree_resolution_()
		if self.degree == 2:
			roots = self._second_degree_resolution_()
		if self.degree == 3:
			roots = self._third_degree_resolution_()
		self.roots = roots
		return roots


	def lambda_polynom(self):
		""" Constructs the lambda function f corresponding to the polynomial.
		Return:
		-------
			f [lambda function]: polynomial function.
		"""
		lst_p = list(range(len(self.coefs)))
		lst_p.reverse()
		f = lambda x: sum([a * power(x, p) for a, p in zip(self.coefs, lst_p)])
		self.lambda_p = f
		return f


	def lambda_first_derivative(self):
		""" Constructs the lambda function df corresponding to the polynomial
		first derivative.
		Return:
		-------
			df [lambda function]: polynomial derivative function.
		"""
		lst_p = list(range(len(self.coefs)))
		lst_p.reverse()
		lst_p = lst_p[:-1]
		d_coeffs = self.coefs[:-1]
		print(f"valeurs de coeffs: {self.coeffs} --- valeurs de d_coeffs = {d_coeffs}")
		print(f"valeurs de lst_p = {lst_p}")
		df = lambda x: sum([a * p * power(x, p - 1) for a, p in zip(d_coefs, lst_p)])
		self.lambda_dp = df
		return df


	def lambda_second_derivative(self):
		""" Constructs the lambda function d2f corresponding to the polynomial
		second derivative.
		Return:
		-------
			d2f [lambda function : polynomial second derivative function.
		"""
		lst_p = list(range(len(self.coefs)))
		lst_p.reverse()
		lst_p = lst_p[:-2]
		d2_coeffs = self.coefs[:-2]
		d2f = lambda x: sum([a * p * (p - 1) * power(x, p - 2) for a, p in zip(d2_coefs, lst_p)])
		self.lambda_d2p = d2f
		return d2f


	@staticmethod
	def _print_roots(roots):
		""" Displays the number in the parameter roots as string. roots
		parameter is expected to be the list of the root of a Polynomial object.
		Parameters:
		-----------
			* roots [list(float/complex)]: list of all the roots of a polynomial
				expression.
		"""
		if len(roots) == 1:
			print("The solution is:")
		else:
			print("The solutions are:")
		for r in roots:
			if isinstance(r, (int, float)):
				print(r)
			if isinstance(r, complex):
				if r.imag > 0:
					print(r.real, '+', f"{r.imag}.j")
				else:
					print(r.real, '-', f"{-r.imag}.j")


	def _summarize_degree_other(self):
		""" Displays type function.
		Function prints:
			* reduced form of the Polynomial instance.
			* natural form of the Polynomial instance.
			* degree of the Polynomial instance.
			* message that computor does not manage the roots seach for
			polynomial degree greater than 3.
		"""
		print("Reduced form:".ljust(20), self.__repr__() + " = 0")
		print("Natural form:".ljust(20), self.natural_form() + " = 0")
		print("Polynomial degree:".ljust(20), self.degree)
		msg = "Resolution of polynomial equation with degree higher " \
			+ "than 3 are not handle in this project."
		print(color.YELLOW + msg + color.NOC)
		self.roots = []


	def _summarize_degree_3(self):
		"""Displays type function.
		The function is here for the completeness of the class and avoid
		the redefinition of the some methods in the class PolynomialBonus.
		"""
		delta = self.discriminant()
		self.roots = []
		
		print("Reduced form:".ljust(20), self.__repr__() + " = 0")
		print("Natural form:".ljust(20), self.natural_form() + " = 0")
		print("Factorized form:".ljust(20), color.YELLOW + "None" + color.NOC)
		print("Polynomial degree:".ljust(20), self.degree)
		print("Discriminant: ".ljust(20), delta)

		msg = "3rd degree resolution is a project's bonus. " \
				+ "Use instance of class PolynomialBonus to have access to " \
				+ "to the resolution of 3rd degree polynomial."
		print(color.YELLOW + msg + color.NOC)
		


	def _summarize_degree_2(self):
		"""Displays type function.
		Function prints:
			* reduced form of the Polynomial instance.
			* natural form of the Polynomial.
			* degree of the Polynomial.
			* discriminant of the Polynomial.
			* roots of the Polynomial.
		"""
		print("Reduced form:".ljust(20), self.__repr__() + " = 0")
		print("Natural form:".ljust(20), self.natural_form() + " = 0")
		print("Factorized form:".ljust(20), self.factorized_form())
		print("Canonical form:".ljust(20), self.canonical_form())
		print("Polynomial degree:".ljust(20), self.degree)
		delta = self.discriminant()
		print("Discriminant:".ljust(20), delta)
		roots = self.polynomial_roots()
		if delta >= 0:
			print("Discriminant is positive, the three real roots are:")
		if delta < 0:
			print("Discriminant is strictly negative, the three roots (1 real + 2 complex) are:")
		Polynomial._print_roots(roots)


	def _summarize_degree_1(self):
		"""Displays type function.
		Function prints:
			* reduced form of the Polynomial instance.
			* natural form of the Polynomial.
			* degree of the Polynomial.
			* root of the Polynomial.
		"""
		print("Reduced form:".ljust(20), self.__repr__(), " = 0")
		print("Factorized form:".ljust(20), self.factorized_form() + " = 0")
		print("Natural form:".ljust(20), self.natural_form() + " = 0")
		print("Polynomial degree:".ljust(20), self.degree)
		roots = self.polynomial_roots()
		Polynomial._print_roots(roots)


	def _summarize_degree_0(self):
		"""Displays type function.
		Function prints:
			* reduced form of the Polynomial instance.
			* natural form of the Polynomial.
			* degree of the Polynomial.
			* root of the Polynomial when it exists.
		"""
		print("Reduced form:".ljust(20), self.__repr__(), " = 0")
		print("Natural form:".ljust(20), self.natural_form() + " = 0")
		print("Polynomial degree:".ljust(20), self.degree)
		roots = self.polynomial_roots()
		if roots[0] is None:
			print("There is no solution for the zeroth order polynomial equation.")
		if roots[0] == 0:
			print("All real values of x are solution of the zeroth order polynomial eqution.")


	def summarize(self):
		"""Displays core function.
		Calls the appropriate display function according to the polynomial degree.
		"""
		if self.degree > 3:
			self._summarize_degree_other()
		elif self.degree == 3:
			self._summarize_degree_3()
		elif self.degree == 2:
			self._summarize_degree_2()
		elif self.degree == 1:
			self._summarize_degree_1()
		elif self.degree == 0:
			self._summarize_degree_0()


	def factorized_form(self):
		""" Returns the factorized expression of the polynomial expression
		in a string format.
		Return:
		-------
			s_poly [str]: factorized expression of the polynomial.
		"""
		roots = self.polynomial_roots()
		signs = [c_sign_(r) for r in roots]
		
		s_poly = f"{self.coefs[0]}"
		for sign, r in zip(signs, roots):
			if isinstance(r, (float, int)):
				if sign == '+':
					s_poly += f" * (X - {abs_(r)})"
				else:
					s_poly += f" * (X + {abs_(r)})"
			if isinstance(r, complex):
				if (sign[0] == '-') and (sign[1] == '-'):
					val = [abs_(r.real), abs_(r.imag)]
					s_poly += f" * (X + {val[0]} + {val[1]}.j)"
				elif (sign[0] == '-') and (sign[1] == '+'):
					val = [abs_(r.real), abs_(r.imag)]
					s_poly += f" * (X + {val[0]} - {val[1]}.j)"
				elif (sign[0] == '+') and (sign[1] == '-'):
					val = [abs_(r.real), abs_(r.imag)]
					s_poly += f" * (X - {val[0]} + {val[1]}.j)"
				else:
					val = [abs_(r.real), abs_(r.imag)]
					s_poly += f" * (X - {val[0]} - {val[1]}.j)"
		if s_poly[0:4] == "1 * ": 
			s_poly = s_poly[4:]
		return  s_poly


	def canonical_form(self):
		""" Returns the canonical expression of the polynomial expression
		in a string format.
		Return:
		-------
			s_poly [str]: canonical expression of the polynomial.
		"""
		alpha = -0.5 * self.coefs[1] / self.coefs[0]
		beta = 0.25 * self.discriminant() / self.coefs[0]
		
		sign1 = '-'
		sign2 = '-'
		if alpha < 0:
			sign1 = '+'
		if beta < 0:
			sign2 = '+'

		alpha = abs_(alpha)
		beta = abs_(beta)
		s_poly = f"{self.coefs[0]} * (X {sign1} {alpha})^2 {sign2} {beta}"
		if s_poly[0:5] == "1 * ":
			s_poly = s_poly[0:5]
		return s_poly


	def natural_form(self):
		""" Returns the natural expression of the polynomial expression
		in a string format.
		Return:
		-------
			s_poly [str]: natural expression of the polynomial.
		"""
		s_poly = self.__repr__()
		s_poly = s_poly.replace('^1', '')
		s_poly = s_poly.replace(' * X^0 ', '')
		s_poly = s_poly.replace('1 * X', 'X')
		return s_poly


	def __repr__(self):
		""" Returns the developped expression of the polynomial expression
		in a string format.
		Return:
		-------
			s_poly [str]: developped expression of the polynomial.
		"""
		# pour afficher la forme developpée.
		lst_p = list(range(len(self.coefs)))
		lst_p.reverse()
		sign = [sign_(c) for c in self.coefs]
		abs_val = [abs_(n) for n in self.coefs]
		if sign[0] == '+':
			sign[0] = ''
		
		s_poly = [f"{s} {c} * X^{p} " for s, c, p in zip(sign, abs_val, lst_p) if c != 0]
		s_poly = ''.join(s_poly)
		if s_poly[0:5] == ' 1 * ':
			s_poly = s_poly[5:]
		if s_poly[0:1] == ' ':
			s_poly = s_poly[1:]
		return s_poly


# =========================================================================== #
# _____________________   |Definition des fonctions |   _____________________ #
# =========================================================================== #
def babylonian_sqrt(nb):
	""" Implementation of the Babylonian square-root algorithm.
	Parameters:
	-----------
		nb [int/float]: number to dermine the square root.
	Return:
	-------
		sqrt : square root of the number nb.
	"""
	if nb < 0:
		nb *= -1
	sqrt = nb / 2
	diff = 1
	while diff > prec:
		prev_guess = sqrt
		sqrt = (sqrt + nb / sqrt) / 2
		diff = prev_guess - sqrt
		if diff < 0:
			diff = -diff
	return sqrt


def binary_search_cubic_root(nb):
	""" Binary search to calcultates the cubic root of nb.
	Parameters:
	-----------
		nb [int/float]: number to dermine the cubic root.
	Return:
	-------
		cub_r : cubic root of the number nb.
	"""
	if nb < 0:
		sign = -1
	else:
		sign = 1
	
	return abs(nb) ** (1/3) * sign
	if sign * nb >= 1: 
		start = 0
		end = sign * nb
	else:
		start = sign * nb
		end = 1
	i = 0
	while True:
		cub_r = 0.5 * (start + end)
		cube = cub_r * cub_r * cub_r
		diff = sign * nb - cube
		if diff < 0:
			diff = -diff
		if diff < prec:
			return sign * cub_r
		if cube > sign * nb:
			end = cub_r
		else:
			start = cub_r
		i += 1


def power(x,p):
	""" Elevates the number x to the power p.
	Arguments:
	----------
		* x [int/float]: a number.
		* p [int]: the power that will elevate x.
	Return:
	-------
		* res [int/float]: result of x**p
	Why?:
	-----
		According to the project pdf, the only authhorized operations
		are '+','-','*' and '/'
	"""
	i = 1
	if p == 0:
		return 1
	res = x
	while i < p:
		res *= x
		i += 1
	return res


def c_sign_(coef: int or float or complex):
	""" Returns the sign of coef.
	Parameters coef can be a int, float or complex.
	If coef is in (int, float), _sign is called, otherwise the signs
	of the real and imaginary parts are returned.
	Return:
	-------
		* '+'/'-' [str]: if coef is (int | float) and positive / negative.
		* ['+'/'-', '+'/'-'] [list]: signs of the real and imaginary part.
	"""
	if isinstance(coef, (int, float)):
		return sign_(coef)
	return [sign_(coef.real), sign_(coef.imag)]


def sign_(coef:int or float) -> str:
	""" Returns the sign of coef. Parameters coef is a float or an int only.
	Return:
	-------
		* '+' [str]: if coef is positive.
		* '-' [str]: if coef is negative.
	"""
	if (coef > 0):
		return '+'
	if (coef < 0):
		return '-'


def c_abs_(nb:int or float or complex):
	""" Returns the absolute value of the coef.
	If coef is an int | float, _abs is called, otherwise absolute value
	of the real and imaginary part are returned.
	Return:
	-------
		* |nb|: if nb is an integer / float.
		* [|nb.real|, |nb.imag|]: if nb is a complex.
	"""
	if isinstance(nb, (int, float)):
		return _abs(nb)
	# there is no absolue value for complex number
	return [_abs(nb.real), _abs(nb.imag)]


def abs_(nb:int or float):
	""" Returns the absolute value of the coef.
	Return:
	-------
		* |nb|.
	"""
	if (nb >= 0):
		return nb
	if (nb < 0):
		return -nb