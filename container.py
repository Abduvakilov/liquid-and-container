class Container:   # angle is not taken into consideration beacause it will not affect to the volume
	def __init__(self, volume):
		self.volume   = volume   # volume in m3
		self.isFilled = False

	def getInput(self, state):
		state = 'Insert {} of {} separated by spaces: '.format(state, self.name)
		arguments     = input(state)
		argumentArray = arguments.strip().split(' ')
		try:
			return (int(argumentArray[0]), int(argumentArray[1]))
		except:
			print("Enter 2 or more numbers, please. Try again")
			self.getInput(state)

	def fill(liquid):
		self.mass     = liquid.density * self.volume
		self.isFilled = True

class SquareContainer(Container):
	name = 'Square prism'
	def __init__(self, edge=None, height=None): # I created an option to give parameters as an argument even if the task does not require it
		if edge is None or height is None:
			edge, height = self.getInput('edge, height and angle')
		self.edge   = edge   # cm
		self.height = height # cm
		self.volume = edge * edge * height

class CircleContainer(Container):
	name = 'Cylinder'
	def __init__(self, radius=None, height=None): # I created an option to give parameters as an argument even if the task does not require it
		if radius is None or height is None:
			radius, height = self.getInput('radius, height and angle')
		self.radius = radius  # cm
		self.height = height  # cm
		self.volume = math.pi * radius * radius * height

class TriangleContainer(Container):   # triangle with equal edges
	name = 'Triangular prism'
	def __init__(self, edge=None, height=None): # I created an option to give parameters as an argument even if the task does not require it
		if edge is None or height is None:
			edge, height = self.getInput('edge, height and angle')
		self.edge   = edge   # cm
		self.height = height # cm
		self.volume = math.sqrt(3)/4 * edge * edge
