from hashlib import sha256
import json
from datetime import datetime
#custom

class Block:
	def __init__(self, index, previous_hash, current_transactions, timestamp, nonce):
		self.index = index
		self.previous_hash = previous_hash
		self.current_transactions = current_transactions
		self.timestamp = timestamp
		self.nonce = nonce
		self.hash = self.compute_hash()
		## initializing the blocks

	def compute_hash(self):
		block_str = json.dumps(self.__dict__, sort_keys=True) #converts python obj (dict) to a JSON str
															 #sort_keys=True places the strs in alphanumeric order
		first_hash = sha256(block_str.encode()).hexdigest()
		second_hash = sha256(first_hash.encode()).hexdigest()
		return second_hash 
		#calculates the hash for a block

	def __str__ (self):
		return str(self.__dict__)


class Blockchain:
	def __init__(self):
		self.chain = []
		self.transactions = []
		self.genesis_block()

		#intializes the chain, transactions, + genesis block

	def __str__(self):
		return str(self.__dict__)


	def genesis_block(self):
		genesis_block = Block('Genesis',0x0, [2,8,9,10,11], 'datetime.now().timestamp()',0) #[2,8,9,10,11] was dummy data
		genesis_block.hash = genesis_block.compute_hash()
		self.chain.append(genesis_block.hash)
		self.transactions.append(str(genesis_block.__dict__))
		return genesis_block

	def getLastBlock(self):
		return self.chain(-1) #returns last element of the blockchain

	def proof_of_work(self, block):
		difficulty = 2
		block.nonce = 0
		computed_hash = block.compute_hash()
		while not (computed_hash.endswith('0'* difficulty) and ('55' * difficulty) in computed_hash):
			#has to end in zero and has to have 55 in there somewhere
			block.nonce += 1
			computed_hash = block.compute_hash()
			return computed_hash

	def add(self, data):
		block = Block(len(self.chain), self.chain[-1], data, 'datetime.now().timestamp()',0)
		block.hash = self.proof_of_work(block)
		self.chain.append(block.hash)
		self.transactions.append(block.__dict__)
		return json.loads(str(block.__dict__).replace('\'','\"'))

	def getTransactions(self, id):
		labels = ['Manufacturer', 'Supplier', 'User', 'Recycling Unit']
		while True:
			try:
				if id == 'all':
					for i in range(len(self.transactions)-1):
						print('{}: \n{}\n'. format(labels[i], self.transactions[i+1]))
					break

				elif type(id) ==int:
					print(self.transactions[id])
					break

			except Exception as e:
				print(e)

def main():
	manufacturer = {
		'transactions':
			[
				{
				'timestamp':datetime.now().timestamp(),
				'product_id': 1,
				'product_serial': 50001000,
				'name': 'cotton pants',
				'from': 'Manufacturer X',
				'to': 'Supplier X',
				'message': 'This product is in good order',
				'digital signiture': 'approved',
				'flagged': 'N'
				},
				{
				'timestamp':datetime.now().timestamp(),
				'product_id': 2,
				'product_serial': 50002000,
				'name': 'cotton pants',
				'from': 'Manufacturer X',
				'to': 'Supplier X',
				'message': 'This product is in good order',
				'digital signiture': 'approved',
				'flagged': 'N'
				}
			]

		}

	supplier = {
		'transactions':
			[
				{
				'timestamp':datetime.now().timestamp(),
				'product_id': 1,
				'product_serial': 50001000,
				'name': 'cotton pants',
				'from': 'Supplier X',
				'to': 'User X',
				'message': 'Product is in order. Shipped',
				'digital signiture': 'approved',
				'flagged': 'N'
				},
				{
				'timestamp':datetime.now().timestamp(),
				'product_id': 2,
				'product_serial': 50002000,
				'name': 'cotton pants',
				'from': 'Supplier X',
				'to': 'User X',
				'message': 'This product is in good order',
				'digital signiture': 'approved',
				'flagged': 'N'
				}
			]
		}

	user = {
		'transactions':
			[
				{
				'timestamp': datetime.now().timestamp(),
				'product_id': 1,
				'product_serial': 50001000,
				'name': 'cotton pants',
				'from': 'User X',
				'to': 'Recycling Unit X',
				'message': 'Product is in order. Shipped',
				'digital signiture': 'approved',
				'flagged': 'N'
				},
				{
				'timestamp':datetime.now().timestamp(),
				'product_id': 2,
				'product_serial': 50002000,
				'name': 'cotton pants',
				'from': 'User X',
				'to': 'Recycling Unit X',
				'message': 'This product is in good order',
				'digital signiture': 'approved',
				'flagged': 'N'
				}
			]
		}

	B = Blockchain()
	a = B.add(manufacturer)
	b = B.add(supplier)
	c = B.add(user)
	B.getTransactions('all')
	return

if __name__ == '__main__':
	main()

