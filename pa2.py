from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify, unhexlify

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AES_CBC_Cipher:
	def __init__(self, KEY):
		self.KEY = KEY

	def encrypt(self, PT):
		PT = pad(PT)
		IV = Random.new().read(AES.block_size)
		cipher = AES.new(self.KEY, AES.MODE_CBC, IV)
		return IV + cipher.encrypt(raw)

	def decrypt(self, CT):
		IV = CT[:16]
		cipher = AES.new(self.KEY, AES.MODE_CBC, IV)
		return unpad(cipher.decrypt(CT[16:]))
		
class AES_CTR_Cipher:
	def __init__(self, KEY):
		self.KEY = KEY

	def encrypt(self, PT):
		PT = pad(PT)
		IV = Random.new().read(AES.block_size)
		CTR = Counter.new(128, initial_value=long(hexlify(IV), 16))
		cipher = AES.new(self.KEY, AES.MODE_CTR, counter=CTR)
		return IV + cipher.encrypt(raw)

	def decrypt(self, CT):
		IV = CT[:16]
		CTR = Counter.new(128, initial_value=long(hexlify(IV), 16))
		cipher = AES.new(self.KEY, AES.MODE_CTR, counter=CTR)
		return cipher.decrypt(CT[16:])		

raw_CT = [
	('140b41b22a29beb4061bda66b6747e14', '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'), 
	('140b41b22a29beb4061bda66b6747e14', '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'), 
	('36f18357be4dbd77f050515c73fcf9f2', '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'), 
	('36f18357be4dbd77f050515c73fcf9f2', '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451')
]
raw_CT = [(a.decode('hex'), b.decode('hex')) for (a, b) in raw_CT]

for (KEY, CT) in raw_CT[:2]:
	cipher = AES_CBC_Cipher(KEY)
	print cipher.decrypt(CT)
	
for (KEY, CT) in raw_CT[2:]:
	cipher = AES_CTR_Cipher(KEY)
	print cipher.decrypt(CT)