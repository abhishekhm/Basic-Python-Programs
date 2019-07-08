import re

def fun(s):
    # return True if s is a valid email, else return False
    if re.match("[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.([a-zA-Z]{1,3}$)", s)!=None:
        return True
    else:
        return False




print(fun('aaa@b.om'))