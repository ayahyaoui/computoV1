from utils import *
from myast import *

"""
    calcul_multiple: recois 2 liste de token et renvoie le proquit ou la 
    quotient de ces listes
    Note: les 2 listes de token sont constituer uniquement de '+'et Monome
    Raise: Si on a une division avec un polinome au denominateur (non unique )
    Raise2: Si on a une division avec 0 au denominateur 
"""
def calcul_multiple(first_operand, second_operand, is_multiple):
    result = []

    if not is_multiple and count_Monome(second_operand) > 1:
        affichage("","","Polynomial divisor", second_operand)
        raise Exception("Polynomial divisor")
    
    for second_token in second_operand:
       
        if isinstance(second_token, MyMonomial):
            for first_token in first_operand:
                if isinstance(first_token, MyMonomial):
                    tmp_result = MyMonomial(first_token.coefficient, first_token.exposant)
                    if is_multiple:
                        tmp_result.multiply_MyMonomial(second_token)
                    else:
                        tmp_result.divide_MyMonomial(second_token)
                    result.append(tmp_result)
    #''' A REVOIR pas besoin de fill avant de simplifier

    result = fill_addition_NPI(result)
    if len(result) > 2:
        for index, elem in enumerate(result):
            elem.group = index
        result = simplification_addition(result)
    return result 


def expression_power(list_token, exposant):
    if exposant > 100:
        affichage("", "", "Attention vous mettez un polinome avec un exposant tres grand")
    decomp_binaire = bin(exposant)[2:][::-1]
    decomp_exposant = [index for index in range(len(decomp_binaire)) if decomp_binaire[index] == '1']
    decomp_value = [2**value for value in decomp_exposant]
    j = 0
    list_factor = []
    if decomp_exposant[0] == 0:
        list_factor = [list_token.copy()]
        j = 1
    
    
    for index in range(decomp_exposant[-1]):
        list_token = calcul_multiple(list_token, list_token.copy(), True)
        if decomp_exposant[j] == index + 1:
            list_factor.append(list_token.copy())
            j += 1

    result = list_factor[0]
    for operand in list_factor[1:]:
        result = calcul_multiple(result, operand, True)
    return result


"""
    VERSION GENIAL (si ca marche)
    Transormation (x+1)^150 en (x+1)ˆ128 * (x+1)^16 * (x+1)ˆ4 * (x+1)ˆ2
                        puis en ((((x+1)ˆ2)ˆ2)ˆ4) ... 
    Nombre de multiplication passe de 149 a 9 !! 
    Complexite pire des cas O( 2 * log(n)) (en nombre de multiplication)
"""
def calcul_powerV2(first_operand, second_operand):
    if len(second_operand) > 1 or not isinstance(second_operand[0], MyMonomial) or second_operand[0].exposant != 0:
        #affichage("", "", "Polynomial exponent or parsing issue" , second_operand[0])
        raise Exception("Polynomial exponent ")
    exposant = second_operand[0].coefficient
    res = first_operand.copy()
    if count_Monome(first_operand) > 1:
        if exposant < 0:
            res = calcul_multiple([MyMonomial(1, 0)], expression_power(first_operand, - exposant), False)
        elif exposant == 0:
            res = [MyMonomial(1, 0)]
        else:
            res = expression_power(first_operand, exposant)
    else:
        elu = [token for token in first_operand if isinstance(token, MyMonomial)][0]
        elu.power_MyMonomial(second_operand[0])
        res = [elu]
    return res


