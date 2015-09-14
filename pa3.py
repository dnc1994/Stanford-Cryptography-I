from Crypto.Hash import SHA256

class StreamHash:
	def __init__(self, filename):
		self.file = open(filename, 'rb')
		self.block_size = 1024
		self.block_list = []
		
	def read_block(self):
		return self.file.read(self.block_size)
		
	def read_all_blocks(self):
		new_block = self.read_block()
		while new_block != '':
			self.block_list.append(new_block)
			new_block = self.read_block()
	
	def compute_hash(self):
		self.read_all_blocks()
		ret = ''
		for block in reversed(self.block_list):
			ret = SHA256.new(block + ret).digest()
		return ret.encode('hex')
		
sh = StreamHash('pa3-submit.mp4')
print sh.compute_hash()