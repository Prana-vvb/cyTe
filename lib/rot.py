def encrypt(msg: str, key: int):
    txt = ''

    for s in msg:
        sIndex = ord(s)
        if s.isalpha():
            if s.isupper():
                tIndex = (sIndex + key - 65)%26 + 65
            else:
                tIndex = (sIndex + key - 97)%26 + 97
            txt += chr(tIndex)
        else:
            txt += s

    return txt

def decrypt(msg: str, key: int):
    txt = ''

    for s in msg:
        sIndex = ord(s)
        if s.isalpha():
            if s.isupper():
                tIndex = (sIndex - key - 65)%26 + 65
            else:
                tIndex = (sIndex - key - 97)%26 + 97
            txt += chr(tIndex)
        else:
            txt += s

    return txt
