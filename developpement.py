from calcul import calcul
from myast import *
from utils import *


def    get_next_operator(list_token):
    for index, value in enumerate(list_token):
        if value.is_operator():
            return index, value
    return -1        

def     pop_last_group(list_token, index):
    group = []
    group_id = list_token[index].group
    while index >= 0 and group_id == list_token[index].group:        
        group.insert(0, list_token.pop(index))
        index -= 1
    return index, group, list_token



"""
    developpement recois une liste de token au format NPI
    Renvois le resultat developper
    soit une liste de token contenant que des Monome et des addition
    (les Monome on tous un exposant different)
"""
def developpement(list_token):
    for index, token in enumerate(list_token):
        token.group = index
    index = 0
    while index < len(list_token):
        first_operand = []
        second_operand = []

        
        while index < len(list_token) and not list_token[index].is_operator():
            index += 1
        
        if index == len(list_token):
            break
        operator = list_token.pop(index)
        index -= 1
        
        index, second_operand, list_token = pop_last_group(list_token, index)
        index, first_operand, list_token = pop_last_group(list_token, index)
        index += 1
        if VERBOSE > 2:
            print(list_token[:index], f"{bcolors.FAIL}",
        first_operand, operator, second_operand,  f"{bcolors.ENDC}", list_token[index:])
        #try:
        tmp_result = calcul(first_operand, second_operand, operator)
        #except:
        #    raise Exception
        if VERBOSE > 2:
            print(list_token[:index], f"{bcolors.OKGREEN}", tmp_result,  f"{bcolors.ENDC}", list_token[index:])
        size_result = len(tmp_result)
        list_token[index:index] = tmp_result
        index += size_result
    return list_token

