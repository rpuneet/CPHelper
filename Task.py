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

	def addTask(self , input , output = ""):
		toRemove = None

		for test in self.taskData['tests']:
			if test['input'].strip() == input.strip():
				if test['output'].strip() == output.strip():
					return
				toRemove = test

		print toRemove
		if toRemove:
			self.taskData['tests'].remove(toRemove)

		self.taskData['tests'].append({'input' : input , 'output':output})
		with open(self.taskBasePath + '.json' , 'wb') as jsonFile:
			json.dump(self.taskData , jsonFile)