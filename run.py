import liquid
import container
import random
import sys
if sys.version_info <= (3, 0):
    sys.stdout.write("Sorry, requires Python 3 or newer\n")
    sys.exit(1)

class randomLiquidsOnContainers:

	liquidTypes  = [liquid.Alcohol(), liquid.Petrol(), liquid.Water()]
	containerTypes = [container.SquareContainer, container.CircleContainer, container.TriangleContainer]
	containers = []

	def chooseLiquid(self):
		count = len(self.liquidTypes)
		import random
		r = random.randint(0, count-1)
		return self.liquidTypes[r]

	def chooseContainers(self):
		counts    = []
		state = "How many %ss do you want to have?   "

		for containerType in self.containerTypes:
			while True:
				try:
					countIn = input(state % containerType.name).strip()
					counts += [int(countIn)]
				except:
					print("Enter a number, please.")
					continue
				break
		return counts

	def __init__(self):
		counts = self.chooseContainers()
		if sum(counts)<5:
			print("Total is less than 5. Enter again, please")
			self.__init__()
		print("\n Insert parameters of containers in centimeter or degrees separated by spaces (leave empty for random generation): ")
		for index, containerType in enumerate(self.containerTypes):
			for i in range(counts[index]):
				self.containers += [containerType()]

	def fillWithLiquid(self):
		for container in self.containers:
			randomLiquid = self.chooseLiquid()
			container.fill(randomLiquid)

	def sortContainers(self):
		self.containers.sort(key=lambda x: x.mass, reverse=True)

	def printTable(self):
		titles = ['Container Type', 'h (cm)', 'a (cm)', 'r (cm)', 'd(deg)', 'V (m3)', 'V (litre)', 'liquid', 'p (kg/m3)', 'm (kg)']
		name   = [x.name for x in self.containers]
		h = [x.height for x in self.containers]
		a = [getattr(x, 'edge', '-') for x in self.containers]
		r = [getattr(x, 'radius', '-') or '-' for x in self.containers]
		d = [x.angle for x in self.containers]
		V = [round(x.volume, 3) for x in self.containers]
		litre = [round(x.litre, 2) for x in self.containers]
		liquid = [x.filledWith for x in self.containers]
		liquidName = [x.filledWith.__class__.__name__ for x in self.containers]
		p = [x.density for x in liquid]
		m   = [round(x.mass, 2) for x in self.containers]

		data     = [titles] + list(zip(name, h, a, r, d, V, litre, liquidName, p, m))
		colWidth = [16,6,6,6,6,10,14,12,10,16]
		print('\n Containers sorted by mass')
		for i, d in enumerate(data):
			line = '|'.join(str(x).ljust(colWidth[c]) for c, x in enumerate(d))
			print(line)
			if i == 0:
				print('-' * len(line))


a = randomLiquidsOnContainers()
a.fillWithLiquid()
a.sortContainers()
a.printTable()