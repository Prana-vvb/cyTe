def encrypt(plaintext: str, key: int):
    plaintext = "".join(plaintext.split())

    rail = [['ph' for i in range(len(plaintext))] for j in range(key)]

    direction_down = False
    col = 0
    row = 0

    for i in range(len(plaintext)):
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = plaintext[i]
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    ciphertext = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != 'ph':
                ciphertext.append(rail[i][j])

    return "".join(ciphertext)

def decrypt(ciphertext: str, key: int):

    rail = [['*' for i in range(len(ciphertext))]
            for j in range(key)]

    direction_down = False
    col = 0
    row = 0

    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = 'mkr'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    idx = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == 'mkr') and
                    (idx < len(ciphertext))):
                rail[i][j] = ciphertext[idx]
                idx += 1

    plaintext = []
    col = 0
    row = 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        plaintext.append(rail[row][col])
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return "".join(plaintext)
