def strxor(a, b):
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

CTstr = '09e1c5f70a65ac519458e7e53f36'
PTstr = 'attack at dawn'
PT2str = 'attack at dusk'

print strxor(strxor(CTstr.decode('hex'), PTstr), PT2str).encode('hex')