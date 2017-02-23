class Character(object):
	# def __init_(self):
	def take_damage(self, points_of_damage):
		self.health -= points_of_damage;		
	def attack(self, enemy):		
		print "%s attacks %s" % (self.name, enemy.name)
		hero.take_damage(self.power);		