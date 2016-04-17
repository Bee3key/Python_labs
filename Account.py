class Account(object):
	num_acc = 0
	
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		Account.num_acc += 1	
	def __del__(self):
		Account.num_acc -= 1
	def deposit(self, amt):
		self.balance = self.balance + amt
	def windrow(self, amt): 
		self.balance = self.balance - amt
	def inquiry(self):
		return self.balance


