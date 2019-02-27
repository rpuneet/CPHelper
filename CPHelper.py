import json

globalData = {}

with open('globals.json' , 'rb') as globalJsonFile:
	globalData = json.load(globalJsonFile)

TEMPLATE = globalData['template']
baseContestPath = globalData['baseContestPath']

from flask import Flask , request , redirect
import json , os , subprocess

app = Flask(__name__)

@app.route('/' , methods = ['POST'])
def getData():
	taskData = json.loads(request.data)

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

	return redirect('/')

app.run(port=8090)
