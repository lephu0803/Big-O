def isEmpty(name):
    if len(name) == 0:
        return True
    else:
        return False

def check_a(email, context='email'):
    if context == 'email':
        if '@' not in email:
            return False
        else:
            return True
    elif context == 'domain':
        if '.' not in email:
            return False
        else:
            return True

def isValidFirstChar(char, context='local'):
    if context == 'local':
        if ('A' <= char and char <= 'Z') or ('a' <= char and char <= 'z') or ('0' <= char and char <= '9'):
            return True
        else:
            return False
    elif context == 'domain':
        if char != '.':
            return True
        else:
            return False

def isValidChar(char, context='local'):
    if context == 'local':     
        if char == '.' or char == '_' or ('A' <= char and char <= 'Z') or ('a' <= char and char <= 'z') or ('0' <= char and char <= '9'):
            return True
        else:
            return False
    elif context == 'domain':
        if char == '.' or ('A' <= char and char <= 'Z') or ('a' <= char and char <= 'z') or ('0' <= char and char <= '9'):
            return True
        else:
            return False

def isDuplicatePoint(domain):
    for i in range(len(domain) - 1):
        if domain[i] == '.' and (domain[i] == domain[i+1]):
            return True
    return False
         

def checkmail(email):
    if not check_a(email):
        return False

    try:
        localPart, domainName = email.split('@')
    except:
        return False

    if isEmpty(localPart):
        return False

    if isEmpty(domainName):
        return False
    # Check local Part
    # Check first char
    if not isValidFirstChar(localPart[0], context='local'):
        return False

    for char in localPart:
        if not isValidChar(char, context='local'):
            return False

    # Check domain Part
    # Check Form
    # 4
    if not check_a(domainName, context='domain'):
        return False

    # 5
    for char in domainName:
        if not isValidChar(char, context='domain'):
            return False
        
    if not isValidFirstChar(domainName[0], context='domain'):
        return False

    if not isValidFirstChar(domainName[-1], context='domain'):
        return False

    if isDuplicatePoint(domainName):
       return False

    return True


email = str(input())
if checkmail(email):
    print('VALID')
else:
    print('INVALID')
