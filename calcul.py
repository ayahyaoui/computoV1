from myast import *
from developpement import *
#from test_dev import developpementv2
from utils import *
from calcul_power import *

"""
    calcul_addition: recois 2 liste de token et renvoie la somme ou la 
    soustraction de ces list
    Note: les 2 listes de token sont constituer uniquement de '+'et Monome
"""
def calcul_addition(first_operand, second_operand, is_add):
    rest_equation = []
    dict_power = {}
    for token in first_operand:
        if isinstance(token, MyMonomial):
            if token.exposant in dict_power:
                affichage("", "", "Probleme doublon le travail a mal ete fait+", token, dict_power[token.exposant], 'ˆ', token.exposant)
            dict_power[token.exposant] = token

        elif token.type_token != dict_tokens['+']:
            affichage("", "", "Probleme signe non attendu ici", first_operand)
            raise Exception 
    for token in second_operand:
        if isinstance(token, MyMonomial):
            if token.exposant in dict_power:
                if is_add:
                    dict_power[token.exposant].add_MyMonomial(token)
                else:
                    dict_power[token.exposant].soustract_MyMonomial(token) 
            else:
                if not is_add:
                    token.coefficient *= -1
                dict_power[token.exposant] = token
        elif token.type_token != dict_tokens['+']:           
            affichage("", "", "Probleme signe non attendu ici", first_operand)
            raise Exception
    result = [value for key, value in dict_power.items()]
    result = fill_addition_NPI(result)
    return result


"""
    ANCIENNE VERSION
    Theoriquement les seules signe possiblement dans first_operand et second_operand
    sont "+" ou "-"
    Dans un premier temp replace les calcul 3+2 => 3+0 
    pour ne pas avoir d'erreur avec les signe en notation polonaise inverse
"""
def calcul_addition2(first_operand, second_operand, is_add):
    rest_equation = []
    
    for i_second in range(len(second_operand)):
        if isinstance(second_operand[i_second], MyMonomial):
            for i_first in range(len(first_operand)):
                if isinstance(first_operand[i_first], MyMonomial) and \
                   first_operand[i_first].exposant == second_operand[i_second].exposant:
                    
                    first_operand[i_first].coefficient += second_operand[i_second].coefficient\
                    if is_add else second_operand[i_second].coefficient * -1
                    second_operand[i_second].coefficient = 0
                    second_operand[i_second].exposant = 0
                    break
    return first_operand + second_operand


"""
       calcul: recois 2 liste de token et un signe renvoie le resultat
       actualise le group du resultat
"""
def calcul(first_operand, second_operand, operator):
    
    group = first_operand[0].group
    test_s = str(first_operand) + ' ' +  str(operator) + ' ' +  str(second_operand)

    try:
        if operator.type_token == dict_tokens['+'] or operator.type_token == dict_tokens['-']:
            coeff = 1 if operator.type_token == dict_tokens['+'] else -1
            result = calcul_addition(first_operand, second_operand, operator.type_token == dict_tokens['+'])
        elif operator.type_token == dict_tokens['*'] or operator.type_token == dict_tokens['/']:
            result = calcul_multiple(first_operand, second_operand, operator.type_token == dict_tokens['*'])
        elif operator.type_token == dict_tokens['ˆ']:
            result = calcul_powerV2(first_operand, second_operand)
        else:
            affichage("", "", "pas encore gerer", operator)
            result = first_operand + second_operand + [operator]
    except Exception as e:
        #print(f)
        affichage("", "", f"{bcolors.FAIL}Error dans le calcul{bcolors.ENDC}", first_operand,operator, second_operand)
        print(f"{bcolors.FAIL}Error", e, f"{bcolors.ENDC}")
        #print(f"{bcolors.ENDC}")
        #result =  [MyMonomial(0, 0)]
        #result[0].group = group
        raise e
        #return result
    for elem in result:
        elem.group = group
    if VERBOSE > 2:
        pass
        #affichage("", "", test_s, '=', result)
        #affichage("", "", first_operand,    str(operator) , second_operand, '=', result)
    return result
