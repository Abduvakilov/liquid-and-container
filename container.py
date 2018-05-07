import math
from random import randint
minLength = 10
maxLength = 100
class Container:   # angle is not taken into consideration beacause it will not affect to the volume
	isFilled = False
	def __init__(self, volume):
		self.volume   = volume   # volume in m3

	def getInput(self, param):
		while True:
			arguments = input(self.name+' - '+param+': ').strip()
			if len(arguments)==0:
				arg1 = randint(minLength, maxLength)
				arg2 = randint(minLength, maxLength)
				arg3 = None
				break
			else:
				try:
					argumentArray = [int(x) for x in arguments.split(' ')]
					arg1 = argumentArray[0]
					arg2 = argumentArray[1]
				except IndexError:
					print("Enter 2 numbers, at least, please. Try again")
					continue
				else:
					arg3 = argumentArray[2] if len(argumentArray)>2 else None
					break
		return (arg1, arg2, arg3)


	def fill(self, liquid):
		self.filledWith = liquid
		self.mass     = liquid.density * self.volume
		self.isFilled = True

class SquareContainer(Container):
	name = 'Square prism'
	def __init__(self, edge=None, height=None, angle=90): # I created an option to give parameters as an argument even if the task does not require it
		if edge is None or height is None:
			edge, height, angle = self.getInput('edge, height and angle (defaults to 90)')
		self.edge   = edge   # cm
		self.height = height # cm
		self.angle  = angle or 90 # degrees
		self.volume = int(edge * edge * height)

class CircleContainer(Container):
	name = 'Cylinder'
	def __init__(self, radius=None, height=None, angle=90): # I created an option to give parameters as an argument even if the task does not require it
		if radius is None or height is None:
			radius, height, angle = self.getInput('radius, height and angle')
		self.radius = radius  # cm
		self.height = height  # cm
		self.angle  = angle or 90 # degrees
		self.volume = int(math.pi * radius * radius * height)

class TriangleContainer(Container):   # triangle with equal edges
	name = 'Triangular prism'
	def __init__(self, edge=None, height=None, angle=90): # I created an option to give parameters as an argument even if the task does not require it
		if edge is None or height is None:
			edge, height, angle = self.getInput('edge, height and angle')
		self.edge   = edge   # cm
		self.height = height # cm
		self.angle  = angle or 90 # degrees
		self.volume = int(math.sqrt(3)/4 * edge * edge)
