def matrix(key, x, y, initial):
    result = list()
    for c in key: #Storing key
        if c not in result:
            if c == 'J':
                result.append('I')
            else:
                result.append(c)

    flag = 0
    for i in range(65, 91): #Storing other characters
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))

    k = 0
    mat = [[initial for i in range(x)] for j in range(y)] #Create matrix
    for i in range(0, 5): #Populate matrix
        for j in range(0, 5):
            mat[i][j] = result[k]
            k += 1
    
    return mat

def locIndex(c, mat): #Get location of each character
    loc = list()
    if c == 'J':
        c = 'I'

    for i, j in enumerate(mat):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc

def disp(msg, mat, n: int):
    res = ''
    i = 0

    while i < len(msg):
        loc = locIndex(msg[i], mat)
        loc1 = locIndex(msg[i + 1], mat)

        if loc[1] == loc1[1]:
            res += "{}{}".format(mat[(loc[0] + n)%5][loc[1]], mat[(loc1[0] + n)%5][loc1[1]]).lower()
        elif loc[0] == loc1[0]:
            res += "{}{}".format(mat[loc[0]][(loc[1] + n)%5], mat[loc1[0]][(loc1[1] + n)%5]).lower()
        else:
            res += "{}{}".format(mat[loc[0]][loc1[1]], mat[loc1[0]][loc[1]]).lower()

        i = i + 2

    return res

def encrypt(msg: str, key: str):
    msg = msg.upper().replace(' ', '')
    key = key.replace(' ', '').upper()
    mat = matrix(key, 5, 5, 0)

    for s in range(0, len(msg) + 1, 2): #Padding
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]

    if len(msg)%2 != 0: #Padding
        msg = msg[:] + 'X'

    return disp(msg, mat, 1)

def decrypt(msg: str, key: str):
    msg = msg.upper().replace(' ', '')
    key = key.replace(' ', '').upper()
    mat = matrix(key, 5, 5, 0)

    return disp(msg, mat, -1)
