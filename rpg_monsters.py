from Character import Character
class Goblin(Character):
	def __init__(self):
		self.name = 'goblin';
		self.health = 6;
		self.power = 2;
	def alive(self):
		return self.health > 0;
		