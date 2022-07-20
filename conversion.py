from myast import MyMonomial, dict_tokens, dict_operator_priority, Token

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

"""
    change les variable et les nombre en monome
    pour que les calcul soit que des operation de monome
"""
def change_number(list_token):
    for index, token in enumerate(list_token):
        if token.type_token == dict_tokens["VARIABLE"]:
            list_token[index] = MyMonomial(1, 1)
        elif token.type_token == dict_tokens["NUMBER"]:
            list_token[index] = MyMonomial(token.value, 0)
    return list_token

def key_type_token(token):
    for key in dict_tokens:
        if token.type_token == dict_tokens[key]:
            return key

"""
    Transforme les nombre negatif 'n' en soustraction '0 - n'
    Transforme multiplication implicite X (1+1) => X * (1 + 1)
                                        2 (1+1) => 2 * (1 + 1)
                                        (1 + 1) (1+1) => (1 + 1) * (1 + 1)
                                        (1 + 1) X => (1 + 1) * X
                                        2 X => 2 * X
                                        X X => X * X
    joute des perentheses quand necessaire lors d'un negatif (diff soustraction)
                                                xˆ-1 => x^(0-1)
                                                xˆ-(...) => xˆ(0-(...))
                                                x*-2 => x*(0-2)
                                                x*-(...) => x*(0-(...))
                                                RECURSIVE
    TODO unit test
        PROBLEME A TESTER -2X => (0-2) * X 
    TODO improve
        CHERCHER D'AUTRE raccourci 
"""
def convert_naturel(list_token):
    result = []
    prev = list_token[0]
    if list_token[0].type_token == dict_tokens['-']:
        result = [Token('0')]
    result.append(list_token[0])
    close_after = -1
    for token in list_token[1:]:
        add_now = True
        if close_after >= 0 and token.is_bracket():
            close_after += 1 if token.type_token == dict_tokens['('] else -1

        # (- or *- >> (0- 
        if  token.type_token == dict_tokens['-'] and \
            (prev.type_token == dict_tokens['('] or prev.is_operator()):
            result += [Token('('), Token('0')]
            add_now = False
            close_after = 0
        elif token.type_token in [dict_tokens['VARIABLE'], dict_tokens['(']] and \
           prev.type_token in [dict_tokens['VARIABLE'], dict_tokens['NUMBER'], dict_tokens[')']]:
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

        elif token.is_operator():
            # Version 2
            index = len(list_conversion) - 1
            # while len(list_conversion) > 0 and list_conversio[-1].is_operator()
            while (index >= 0 and list_conversion[index].is_operator()):
                if priority_cmp(token, list_conversion[index]) <= 0:
                    list_result.append(list_conversion.pop(index))
                index -= 1
            list_conversion.append(token)
        elif token.type_token == dict_tokens['(']:
            list_conversion.append(token)
            nb_open_bracket += 1
        elif token.type_token == dict_tokens[')']:
            if nb_open_bracket == 0:
                raise Exception("Probleme de parenthese !! (aurais du être rerperé plus tôt!)")
                return False # A changer (catch ...)

            #Version 2
            index = len(list_conversion) - 1
            while (index > 0 and list_conversion[index].type_token != dict_tokens['(']):
                list_result.append(list_conversion.pop(index))
                index -= 1
            if  dict_tokens['('] != list_conversion.pop(-1).type_token: # eject last open parenthesis
                raise Exception("Probleme de parenthese !! (aurais du être rerperé plus tôt!)")
            nb_open_bracket -= 1
        else:# Issue
            print("Unknown", token.type_token == dict_tokens["UNKNOWN"])
            raise Exception(token.value,"Probleme pas encore geré")
    list_result += list_conversion[::-1]
    for index, token in enumerate(list_result):
        token.group = index
    return list_result

