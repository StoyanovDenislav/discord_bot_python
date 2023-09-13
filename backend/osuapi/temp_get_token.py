def getToken():
    f = open("token.txt", "r")
    return f.read()

def getRefreshToken():
    f = open("refresh_token.txt", "r")
    return f.read()