def BinarySearch(li, num): 
    try:
        the_center = 0
        n1 = 0
        n2 = len(li) - 1
    
        while n1 <= n2: 
            the_center = round((n2 + n1) / 2)
    
            if li[the_center] > num: 
                n2 = the_center - 1
    
            elif li[the_center] < num: 
                n1 = the_center + 1
    
            else: 
                return the_center 
    
        return -1

    except Exception as errorr:
        print('nice error wallah')