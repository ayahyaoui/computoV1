from myast import MyMonomial, dct_tokens, dict_operator_priority, is_operator, Token

#import ast
"""
"""
def priority_cmp(first_operator, second_operator):
    if first_operator.group > second_operator.group:
        return 1
    elif first_operator.group < second_operator.group:
        return -1
    first_value = dict_operator_priority[first_operator.value]
    second_value = dict_operator_priority[second_operator.value]
    
    if first_value > second_value: 
        return 1
    elif first_value < second_value:
        return -1
    else:
        return 0

def change_number(list_token):
    for index, token in enumerate(list_token):
        if token.type_token == dct_tokens["VARIABLE"]:
            list_token[index] = MyMonomial(1, 1)
        elif token.type_token == dct_tokens["NUMBER"]:
            list_token[index] = MyMonomial(token.value, 0)
    return list_token

def key_type_token(token):
    for key in dct_tokens:
        if token.type_token == dct_tokens[key]:
            return key

"""
    Transforme les nombre negatif 'n' en soustraction '0 - n'
    Transforme multiplication implicite X (1+1) => X * (1 + 1)
                                        2 (1+1) => 2 * (1 + 1)
                                        (1 + 1) (1+1) => (1 + 1) * (1 + 1)
                                        (1 + 1) X => (1 + 1) * X
                                        2 X => 2 * X
                                        X X => X * X
    TODO ajouter des perenthse quand necessaire lors d'un negatif (diff soustraction)
                                                xˆ-1 => x^(0-1)
                                                xˆ-(...) => xˆ(0-(...))
                                                RECURSIVE
    PROBLEME A TESTER -2X => (0-2) * X 
    CHERCHER D'AUTRE raccourci 
"""
def convert_naturel(list_token):
    result = []
    prev = list_token[0]
    if list_token[0].type_token == dct_tokens['-']:
        result = [Token('0')]
    result.append(list_token[0])
    close_after = -1
    for token in list_token[1:]:
        add_now = True
        if close_after >= 0 and token.type_token in [dct_tokens['('], dct_tokens[')']]:
            close_after += 1 if token.type_token == dct_tokens['('] else -1

        if  token.type_token == dct_tokens['-'] and \
            (prev.type_token == dct_tokens['('] or is_operator(prev)):
            result += [Token('('), Token('0')]
            add_now = False
            close_after = 0
        elif token.type_token in [dct_tokens['VARIABLE'], dct_tokens['(']] and \
           prev.type_token in [dct_tokens['VARIABLE'], dct_tokens['NUMBER'], dct_tokens[')']]:
            result.append(Token('*'))

        result.append(token)
        if add_now and close_after == 0:
            result.append(Token(')'))
            close_after = -1

        prev = token

    return result

def convert_expression(list_token):
    list_result = []
    list_conversion = []
    nb_open_bracket = 0
    list_token = convert_naturel(list_token)
    list_token = change_number(list_token)
    for token in list_token:
        token.group = nb_open_bracket
        if isinstance(token, MyMonomial):
            list_result.append(token)

        elif is_operator(token):
            # Version 2
            index = len(list_conversion) - 1
            while (index >= 0 and is_operator(list_conversion[index])):
                if priority_cmp(token, list_conversion[index]) <= 0:
                    list_result.append(list_conversion.pop(index))
                index -= 1
            list_conversion.append(token)
        elif token.type_token == dct_tokens['(']:
            list_conversion.append(token)
            nb_open_bracket += 1
        elif token.type_token == dct_tokens[')']:
            if nb_open_bracket == 0:
                raise Exception("Probleme de parenthese !!")
                return False # A changer (catch ...)

            #Version 2
            index = len(list_conversion) - 1
            while (index >= 0 and list_conversion[index].type_token != dct_tokens['(']):
                list_result.append(list_conversion.pop(index))
                index -= 1
            list_conversion.pop(-1) # eject last open parenthesis
            nb_open_bracket -= 1
        else:# Issue
            print("Unknown", token.type_token == dct_tokens["UNKNOWN"])
    list_result += list_conversion[::-1]
    for index, token in enumerate(list_result):
        token.group = index
    return list_result

