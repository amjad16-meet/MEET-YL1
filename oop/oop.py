class Animal:
	def __init__(self,name,color,size,age):
		self.name=name
		self.color=color
		self.size=size
		self.age=age

	def print_all(self):
		print(self.name)
		print(self.color)
		print(self.size)
		print(self.age)

Dog=Animal(name="max",color="red",size="huge",age=5)
Lion=Animal(name="rex",color="black",size="large",age=8)

Dog.print_all()
print("######")
Lion.print_all()
