# =========================================================================== #
# ____________________  |Importation des lib/packages|   ____________________ #
# =========================================================================== #
from polynomial import Polynomial, babylonian_sqrt, binary_search_cubic_root, power

# =========================================================================== #
# ______________________   |Definition des classes |   ______________________ #
# =========================================================================== #

class PolynomialBonus(Polynomial):
	
	def _third_degree_resolution_(self):
		"""
		Calculates the roots of polynomial of degree 3.
		The method is the general cubic formulation deduced from Cardano's formula.
		(wiki source)
		Return:
		-------
			* r... [floats/complexes]: roots of the polynomial.
		"""
		# reference: https://fr.wikiversity.org/wiki/Équation_du_troisième_degré/Méthode_de_Cardan
		if self.degree == 3:
			# Point important: n'est traité que le cas où les coefficients sont réels
			a = self.coefs[0]
			b = self.coefs[1]
			c = self.coefs[2]
			d = self.coefs[3]
			p = c/a - power(b, 2) / (3 * a * a)
			q = (2 * b * b * b - 9 * a * b * c + 27 * a * a * d) / (27 * a * a * a)
			delta_Cardan = - (4 * p * p * p + 27 * q * q)
			j = 0.5 * complex(-1, babylonian_sqrt(3))
			if delta_Cardan == 0:
				r0 = 3 * (q / p) - b / (3 * a)
				r1 = r2 = - 1.5 * (q / p) - b / (3 * a)
			if delta_Cardan > 0:
				u = 0.5 * complex(-q, babylonian_sqrt(delta_Cardan / 27))
				u = u ** (1/3)
				r0 = u + u.conjugate() - (b / (3 * a))
				r1 = j * u + (j * u).conjugate() - (b / (3 * a))
				r2 = j * j * u + (j * j * u).conjugate() - (b / (3 * a))
				r0 = r0.real
				r1 = r1.real
				r2 = r2.real
			if delta_Cardan < 0:
				r0 = binary_search_cubic_root(0.5 * (-q + babylonian_sqrt(-delta_Cardan/27))) \
					+ binary_search_cubic_root(0.5 * (-q - babylonian_sqrt(-delta_Cardan/27))) \
						- b / (3 * a)
				r1 = j * binary_search_cubic_root(0.5 * (-q + babylonian_sqrt(-delta_Cardan/27))) \
					+ j * j * binary_search_cubic_root(0.5 * (-q - babylonian_sqrt(-delta_Cardan/27))) \
						- b / (3 * a)
				r2 = j * j * binary_search_cubic_root(0.5 * (-q + babylonian_sqrt(-delta_Cardan/27))) \
					+ j * binary_search_cubic_root(0.5 * (-q - babylonian_sqrt(-delta_Cardan/27))) \
						- b / (3 * a)
			return [r0, r1, r2]
		else:
			print("Polynomial is not of 3rd degree.")


	def _summarize_degree_3(self):
		"""Displays type function.
		Function prints:
			* reduced form of the Polynomial instance.
			* natural form of the Polynomial.
			* degree of the Polynomial.
			* discriminant of the Polynomial.
			* delta0, delta1 and Cardano coefficient of the Polynomial.
			* roots of the Polynomial.
		"""
		print("Reduced form:".ljust(20), self.__repr__() + " = 0")
		print("Natural form:".ljust(20), self.natural_form() + " = 0")
		print("Factorized form:".ljust(20), self.factorized_form())
		print("Polynomial degree:".ljust(20), self.degree)
		delta = self.discriminant()
		r = self._third_degree_resolution_()
		print(f"Discriminant:".ljust(20), delta)
		if delta < 0:
			print("Discriminant is strictly negative, the real root and the 2 complex roots are:")
		elif delta == 0:
			print("Discriminant is null, the roots are all real and are:")
		else:
			print("Discriminant is strictly positive, the three solutions are:")
		Polynomial._print_roots(r)