# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    process_calcul.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anyahyao <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/23 17:52:01 by anyahyao          #+#    #+#              #
#    Updated: 2021/07/23 17:54:05 by anyahyao         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from test_conversion_npi import *
'''
def     calcul_addition(first_operand, second_operand, is_add):
    for first in first_operand:
        can_add = False
        if first.type_token == VARIABLE_X or first.type_token == DIGIT:
            for index_second in range(len(second_operand)):
                if first.type_token == second_operand[index_second].type_token \
                and first.exposant == second_operand[index_second].exposant:
                    second_operand[index_second].coefficient += first.coefficient \
                    if is_add else first.coefficient * -1
                    can_add = True
                    break
        if not can_add:
            pass
    return True

def  calcul_power(first_operand, second_operand):
    return True

def calcul_multiple(first_operand, second_operand, is_multiple):
    return True


def     calcul_NPI(first_operand, second_operand, operator):
    affiche_list_tokens(first_operand, "first operand:")
    affiche_list_tokens(second_operand, "second operand:")
    print("operator", operator)

    if operator.type_token == OPERATOR_PLUS or operator.type_token>OPERATOR_MINUS:
        calcul_addition(first_operand, second_operand, operator.type_token == OPERATOR_PLUS)
    elif operator.type_token == OPERATOR_MULTIPLE or operator.type_token>OPERATOR_DIVID:
        calcul_multiple(first_operand, second_operand, operator.type_token == OPERATOR_MULTIPLE)
    return first_operand + second_operand + [operator]


def     developpement(list_token):
    #group = list(range(len(list_token)))
    #operator 
    index = 0
    list_token_copy = list_token.copy()

    affiche_list_tokens(list_token, "list start")
    while index < len(list_token) and index < 42:
        first_operand = []
        second_operand = []
        while index < len(list_token) and not list_token[index].is_operator():
            index += 1
        if not list_token[index].is_operator():
            break
        operator = list_token.pop(index)
        index -= 1
        group_second = list_token[index].group
        while group_second == list_token[index].group:
            #print("index avant operator", index, list_token[index].group, list_token[index].value)
            second_operand.insert(0, list_token.pop(index))
            index -= 1
        group_first = list_token[index].group
        while index >= 0 and group_first == list_token[index].group:
            #print("index avant operator 2 ", index, list_token[index].group, list_token[index].value)
            first_operand.insert(0, list_token.pop(index))
            index -= 1
        index += 1
        #affiche_list_tokens(second_operand, "second_operand debut")
        #affiche_list_tokens(first_operand, "first_operand debut")
        tmp = calcul_NPI(first_operand, second_operand, operator)
        size_calcul = len(tmp)
        list_token[index:index] = tmp
        for elem in tmp:
            elem.group = tmp[0].group
        index += size_calcul
        print("end loop index", index, len(list_token))
        affiche_list_tokens(list_token, "result end loop")
    print("END")
'''
