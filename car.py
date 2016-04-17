class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

		
class Acc(object):
	num_acc = 0
	
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		Acc.num_acc += 1

my_car = Car("DeLorean", "silver", 88)
my_acc = Acc("First", 111)


