def is_leap(year):
    
    # variable to check the leap year
    leap = False
    
    # divided by 100 means century year
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        
       # change leap to True
        leap = True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        
        #Change leap to true
        leap = True

    #else not a leap year
    else:      
        pass
    
    return leap