import binascii

def strxor(a, b):
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

A = ['7b50baab07640c3d', '7c2822ebfdc48bfb', 'e86d2de2e1387ae9', '9d1a4f78cb28d863']
B = ['ac343a22cea46d60', '325032a9c5e2364b', '1792d21db645c008', '75e5e3ea773ec3e6']

for (a, b) in zip(A, B):
	print strxor(a.decode('hex'), b.decode('hex')).encode('hex')
