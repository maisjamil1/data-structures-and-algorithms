def left_join(dict1,dict2):
    
    output = []

    for key in dict1.keys():
       if key in dict2.keys():

           output.append([key,dict1[key],dict2[key]])

       else:

           output.append([key,dict1[key],None])


    return output




if __name__ == "__main__":
    #synonym 
    dict1 = {'fond':'enamored',
    'wrath':'anger',
    'diligent':'employed',
    'outfit':'garb',
    'guide':'usher'}

    #antonym
    dict2 = {'fond':'averse',
    'wrath':'delight',
    'diligent':'idle',
    'guide':'follow',
    'flow':'jam'}
    print(left_join(dict1,dict2))