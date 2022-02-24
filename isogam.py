def is_isogram(string):
    string=string.lower()
    for i in string:
        if((i>='a' and i<='z')):
            if(string.count(i)>1):
                return(False)
    return(True)