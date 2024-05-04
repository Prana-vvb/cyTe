def keyGen(str: str, key: str): #Repeat key to match the length of the input text
	key = list(key)
	if len(str) == len(key):
		return(key)
	else:
		for i in range(len(str) -
					len(key)):
			key.append(key[i % len(key)])
	return ''. join(key)
	
def encrypt(msg: str, key: str):
	msg = msg.replace(' ', '').upper()
	key = keyGen(msg, key).upper()
	txt = []
	
	for i in range(len(msg)):
		x = (ord(msg[i]) +
			ord(key[i])) % 26
		x += ord('A')
		txt.append(chr(x))
	
	res = (''.join(txt)).lower()
	return res
	

def decrypt(msg: str, key: str):
	msg = msg.replace(' ', '').upper()
	key = keyGen(msg, key).upper()
	txt = []
	for i in range(len(msg)):
		x = (ord(msg[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		txt.append(chr(x))

	res = (''.join(txt)).lower()
	return res
