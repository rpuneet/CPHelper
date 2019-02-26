import json , os

class Task:
	def __init__(self , taskBasePath):
		self.taskBasePath = taskBasePath
		self.taskData = {}

		if os.path.exists(self.taskBasePath + '.json'):
			with open(self.taskBasePath + '.json') as jsonFile:
				self.taskData = json.load(jsonFile)
		else:
			self.taskData['tests'] = []

	def getData(self):
		return self.taskData

	def getTests(self):
		return self.taskData['tests']

	def addTask(self , input , output):
		pass