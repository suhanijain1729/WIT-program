def classify(number):
    s=0
    if(number>0):
        for i in range(1,number):
            if(number%i==0):
                s=s+i
        if(s==number):
            return('perfect')
        elif(s>number):
            return('abundant')
        else:
            return('deficient')
    else:
        raise ValueError("Classification is only possible for positive integers.")