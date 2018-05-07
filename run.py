import liquid
import container
import random

class randomLiquidsOnContainers:
	liquidTypes  = [liquid.Alcohol(), liquid.Petrol(), liquid.Water()]
	class Containers: 
		types = [container.SquareContainer, container.CircleContainer, container.TriangleContainer]
		counts    = []
		containers= []
		def addCount(self, count):
			self.counts += [int(count.strip())] # adds to the array
		def getTotal(self):
			return sum(self.counts)
		def __init__(self):
			state = "How many {}s do you want to have?\n"
			for containerType in self.types:
				while True:
					try:
						self.addCount(input(state.format(containerType.name)))
					except:
						print("Enter a number, please.")
						continue
					break

	def __init__(self):
		cont = self.Containers()
		if cont.getTotal()<5:
			print("Total is less than 5. Enter again, please")
			self.__init__()
		for index, containerType in enumerate(cont.types):
			cont.containers += [containerType] * counts[index]

a = randomLiquidsOnContainers()