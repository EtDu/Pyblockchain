import hashlib
import json
from pprint import pprint

class Block():
    def __init__(self, index, time_stamp, data, previous_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.time_stamp = time_stamp
        self.data = data
        self.hash = self.calculate_hash()

    nonce = 0

    def calculate_hash(self):
        return hashlib.sha256((f"{self.index} {self.previous_hash} {self.time_stamp} {json.dumps(self.data)} {self.nonce}").encode()).hexdigest()

    def mine_block(self, difficulty):
        zeroes = ""
        i = 0
        while i < difficulty:
            zeroes += "0"
            i += 1
        while self.hash[:difficulty] != zeroes:
            self.nonce += 1
            self.hash = self.calculate_hash()



    
class Blockchain():
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
    
    def create_genesis_block(self):
        return Block(0, "01/01/2018", "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[len(self.chain)-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        i = 0
        while i < len(self.chain) and i > 0:
            self.current_block = self.chain[i]
            self.previous_block = self.chain[i - 1]
            if self.current_block.hash != current_block.calculate_hash:
                return False
            if self.current_block.previous_hash != self.previous_block.hash:
                return False
            i += 1
        return True
        



freedom_coin = Blockchain(4)
print("Mining block one...")
freedom_coin.add_block(Block(1, "1,1", {"statement" : "Freedom for all!"}, ''))
print("Mining block two...")
freedom_coin.add_block(Block(2, "1,1", {"statement" : "Freedom for all!"}, ''))

def print_chain():
    for obj in freedom_coin.chain:
        pprint(vars(obj))

print_chain()







    



