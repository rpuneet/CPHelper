from flask import Flask , request , redirect
import json , subprocess
import datetime
import os

PORT = 7175

def createNewTask(data):

	now = datetime.datetime.now()
	TEMPLATE = globalData['template']
	baseContestPath = globalData['baseContestPath']

	templateHeader = "/*\n"
	templateHeader += 'Author : {}\n'.format(globalData['author'])
	templateHeader += 'Team : {}\n'.format(globalData['teamName'])
	templateHeader += '{}\n'.format(now.strftime("Date : %d-%m-%Y\nTime : %H:%M:%S"))
	templateHeader += '*/\n\n'
	TEMPLATE = templateHeader + TEMPLATE

	taskData = json.loads(data)

	contestName = taskData['group']
	taskName = taskData['name']

	temp = ""
	for x in contestName.split(' '):
		temp += x

	contestName = temp

	temp = ""
	for x in taskName.split(' '):
		temp += x

	taskName = temp

	if not os.path.exists(os.path.join(baseContestPath , contestName , taskName + '.json')):

		if not os.path.exists(os.path.join(baseContestPath , contestName)):
			os.mkdir(os.path.join(baseContestPath , contestName))

		with open(os.path.join(baseContestPath , contestName , taskName + '.json') , 'wb') as taskJsonFile:
			json.dump(taskData , taskJsonFile)
		
		with open(os.path.join(baseContestPath , contestName , taskName + '.cpp') , 'wb') as taskCppFile:
			taskCppFile.write(TEMPLATE)

		print subprocess.check_output(['subl' , os.path.join(baseContestPath , contestName , taskName + '.cpp')])


globalData = {}

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)) , 'globals.json') , 'rb') as globalJsonFile:
	globalData = json.load(globalJsonFile)
	

app = Flask(__name__)

@app.route('/' , methods = ['POST'])
def getData():
	createNewTask(request.data)
	return redirect('/')

app.run(port=PORT)
