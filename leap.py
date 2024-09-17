def is_leap(year):
    leap = False
    
    # Write your logic here
    
    return leap
    
    
    
    
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
   

year = int(input())
print(is_leap(year))