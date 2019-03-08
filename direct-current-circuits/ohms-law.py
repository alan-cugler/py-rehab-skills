def ohms_law(v=None,i=None,r=None): 
    if ((i == None and v == None) or 
       (i == None and r == None) or 
       (r == None and v == None) or 
       (i == None and v == None and r == None) or 
       (i != None and v != None and r != None)): 
        print('Error: Only two variables should be specified.') 
        return 
    if v != None and i != None: 
        result = v/i 
    elif v != None and r != None: 
        result = v/r 
    elif i != None and r != None: 
        result = i*r
    return result
