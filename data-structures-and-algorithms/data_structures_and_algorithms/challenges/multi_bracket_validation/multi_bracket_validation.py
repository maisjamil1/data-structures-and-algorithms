def multi_bracket_validation(input):
    """
    this function will take a string as its only argument, and should 
    return a boolean representing whether or not the brackets in the
     string are balanced. 
    """

    parentheses_R=input.count('(')
    parentheses_L=input.count(')')
    curly_braces_R=input.count('{')
    curly_braces_L=input.count('}')
    bracket_R=input.count('[')
    bracket_L=input.count(']')
    try:
        if bracket_R != bracket_L and curly_braces_R != curly_braces_L:

            print("error closing }. Doesn’t match opening [")
            return False

        elif bracket_R != bracket_L:
            return False
        elif curly_braces_R != curly_braces_L:

            if curly_braces_R>curly_braces_L:
                print("error unmatched opening { remaining.")

            return False
        elif parentheses_R != parentheses_L:

            if parentheses_L> parentheses_R:
                print("error closing ) arrived without corresponding opening.")

            return False

        else:
            return True
    except Exception as err:
            print(f'error ::: {err}')


if __name__ == '__main__':
    pass#to avoid an error in the test file
    # print(multi_bracket_validation('(dd)gggg{ '))
    # print(multi_bracket_validation('test'))
    # print(multi_bracket_validation(')'))
    # print(multi_bracket_validation('{'))
    # print(multi_bracket_validation('}['))
    # print(multi_bracket_validation('('))
    # print(multi_bracket_validation('[blablablal'))

