# import re


# def multi_bracket_validation(input):
#     """
#     this function will take a string as its only argument, and should 
#     return a boolean representing whether or not the brackets in the
#      string are balanced. 
#     """

#     parentheses_R=input.count('(')
#     parentheses_L=input.count(')')
#     curly_braces_R=input.count('{')
#     curly_braces_L=input.count('}')
#     bracket_R=input.count('[')
#     bracket_L=input.count(']')
#     try:
#         if bracket_R != bracket_L and curly_braces_R != curly_braces_L:

#             print("error closing }. Doesn’t match opening [")
#             return False

#         elif bracket_R != bracket_L:
#             return False
#         elif curly_braces_R != curly_braces_L:

#             if curly_braces_R>curly_braces_L:
#                 print("error unmatched opening { remaining.")

#             return False
#         elif parentheses_R != parentheses_L:

#             if parentheses_L> parentheses_R:
#                 print("error closing ) arrived without corresponding opening.")

#             return False

#         else:

#                 # strr='(gfgfgf) {sfsf} [dfd]'
#                 li=[]
#                 regerx = re.findall(r'\[.*?\]', strr)
#                 li2=[]
#                 regerx2 = re.findall(r'\{.*?\}', strr)
#                 li3=[]
#                 regerx3 = re.findall(r'\(.*?\)', strr)

#                 for i in regerx:
#                         li.append(i.strip("{ }"))    
#                 for i in regerx2:
#                         li2.append(i.strip("{ }"))    
#                 for i in regerx3:
#                         li3.append(i.strip("{ }"))  

#                 if li.count('(')==li.count(')') and li.count('[')==li.count(']') and li.count('{')==li.count('}'):
#                     return True
#                 elif li2.count('(')==li2.count(')') and li2.count('[')==li2.count(']') and li2.count('{')==li2.count('}'):
#                     return True
#                 elif li3.count('(')==li3.count(')') and li3.count('[')==li3.count(']') and li3.count('{')==li3.count('}'):
#                     return True
#                 else:
#                     return True
            
    # except Exception as err:
    #         print(f'error ::: {err}')





#Code review
def multi_bracket_validation(input):
    """
    this function will take a string as its only argument, and should 
    return a boolean representing whether or not the brackets in the
     string are balanced. 
    """
    try:
        open_tags = ["[","{","("] 
        closing_tags = ["]","}",")"] 
        check = [] 
            
        for i in input: 

                if i in open_tags: 
                    check.append(open_tags.index(i)) 

                elif i in closing_tags: 
                    if ((len(check) > 0) and (closing_tags.index(i) == check[-1])): 
                        check.pop() 
                    else: 
                        return False

        if len(check) == 0: 
                return True
        else: 
                return False
    except Exception as err :
            print(f'error ::: {err}')



if __name__ == '__main__':
    # pass#to avoid an error in the test file
    # print(multi_bracket_validation('(dd)gggg{ '))
    # print(multi_bracket_validation('test'))
    # print(multi_bracket_validation(')'))
    # print(multi_bracket_validation('{'))
    print(multi_bracket_validation('({)}'))
    # print(multi_bracket_validation('}['))
    # print(multi_bracket_validation('('))
    # print(multi_bracket_validation('[blablablal'))

