class weapon(item):
<<<<<<< HEAD
	def __init__(self, name, value, damage):
		super().__init__(name, value)
		self.damage=damage
=======

	def __init__(self, name, value, damage):
		super().__init__(name, value)
		self.damage=damage
		isBroken=false
>>>>>>> master

	def __str__(self):
		return ""

	def getName(self):
		return self.name

	def getValue (self):
		return self.value

	def setName(self, name):
		self.name=name

	def setValue(self, value):
		self.value=value

	def setDamage(self, damage):
<<<<<<< HEAD
		self.damage=damage
=======
		self.damage=damage

	def destroy(self):
		self.isBroken=true

	def isBroken(self):
		return self.isBroken
>>>>>>> master
