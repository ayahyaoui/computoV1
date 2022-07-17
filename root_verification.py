from sympy import *
from sympy import roots, solve_poly_system
from computor import process_polynom
import sys
from myast import MyMonomial, VERBOSE
from random import randint, random
from utils import *



def transform_solution(my_solution):
    my_solution = [complex(value) for value in my_solution]
    my_solution = [complex(round(value.real, 5), round(value.imag, 5)) for value in my_solution]
    my_solution = sorted(my_solution, key=lambda val: (val.real, val.imag))
    my_solution = [my_solution[0]] + [elem for index, elem in enumerate(my_solution[1:]) if my_solution[index].real != elem.real or my_solution[index].imag != elem.imag]
    return my_solution
def verif_resultat(solution, my_solution):
    
    if len(solution) != len(my_solution):
        print ("Erreur resultat attendue",  solution)
        return False

    
    for my_root, root in zip(my_solution, solution):
        if round(root.real - my_root.real, 3) != 0 or round(root.imag - my_root.imag, 3) != 0:
            if VERBOSE > 2:
                print("diff for ", root, "vs", my_root)
            return False

    
    #print("racine::", )
    return True

def generate_monoms_list():
    #TODO  generer des polynomes plus complexes
    #return [MyMonomial(randint(-5,5), 3), MyMonomial(randint(-5,5), 2), MyMonomial(randint(-5,5),1), MyMonomial(randint(-5,5),0)]
    return [MyMonomial(round(random() * 10 - 5, 5), 3), MyMonomial(round(random() * 10 - 5, 5), 2), MyMonomial(round(random() * 10 - 5, 5),1), MyMonomial(round(random() * 10 - 5, 5),0)]

def test_polynome(lim_test):
    sucess = 0
    test = [[MyMonomial(-3.47569, 3), MyMonomial(4.9709, 2), MyMonomial(-2.37235, 1), MyMonomial(3.84465, 0)],
            [MyMonomial(-3.8962, 3), MyMonomial(4.82772, 2), MyMonomial(-2.03499, 1), MyMonomial(-4.645, 0)],
            [MyMonomial(0.86918, 3), MyMonomial(-2.99614, 2), MyMonomial(3.45002, 1), MyMonomial(4.07312, 0)]]
    for i in range(lim_test):
        if i < len(test):
            list_monoms = test[i]
        else:
            list_monoms = generate_monoms_list()
        equation = ' + '.join([str(elem.coefficient) + ' * X ** ' + str(elem.exposant) for elem in list_monoms])
        print(list_monoms)
        solution = solve(equation)
        solution = [complex(elem) for elem in solution]
        solution = sorted(solution, key=lambda val: (val.real, val.imag))
        polynom = process_polynom(list_monoms)
        my_solution = polynom.polynomial_roots()
        my_solution = transform_solution(my_solution)
        if my_solution is None:
            print("Not a polynome degrees 3", equation)
            print(solution)
        elif verif_resultat(solution, my_solution):
            sucess += 1
            print(f"{bcolors.OKGREEN} Success {i} / {lim_test} {bcolors.ENDC}")
            if VERBOSE > 3 and lim_test < 10:
                print(list_monoms)
                print("Solution::   ", solution)
                print("My solution::", my_solution)
        else:
            last_error = [list_monoms, solution, my_solution]
            print(f"{bcolors.FAIL} Fail {i} / {lim_test} {bcolors.ENDC}")
            if VERBOSE > 2 and lim_test < 50:
                print(list_monoms)
                print("Solution::   ", solution)
                print("My solution::", my_solution)
    if sucess == lim_test:
        print(f"{bcolors.OKGREEN}", "Success", sucess, "/", lim_test, f"{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}", "RESULTAT", sucess, "/", lim_test, f"{bcolors.ENDC}")
    if (VERBOSE < 3  or lim_test >= 10) and sucess < lim_test:
        print("Derniere erreur::", last_error[0])
        print("Solution::   ", last_error[1])
        print("My solution::", last_error[2])







# =========================================================================== #
# ______________________________    |MAIN|     ______________________________ #
# =========================================================================== #
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        test_polynome(4200)    
        sys.exit()
