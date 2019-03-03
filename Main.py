# -*- coding: utf-8 -*-
from CPPCompiler import CPPCompiler		# For compiling and running cplusplus code
from Task import Task 					# For getting task data like test cases
import sys								# For system arguments and exit 
import time								# For calculating runtime of a program.
import os
import json

BASE_PATH = sys.argv[1]					# Base path of the cpp and json file i.e. path of file without extension.

globalData = {}

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)) , 'globals.json') , 'rb') as globalJsonFile:
	globalData = json.loads(globalJsonFile.read().decode())

DASH_COUNT = globalData['dashCount']	# Number of dashes to print after each test case.
inputTxtPath = globalData['inputTxtPath']
TEMPLATE = globalData['template']


compiler = CPPCompiler(BASE_PATH)		# cplusplus compiler.	
task = Task(BASE_PATH)					# task object to get task data

# Compile the cpp file and create a output file. Exception for Compilation error.
try:
	compileOutput = compiler.compile()
except:
	print("Compilation Error")
	exit(0)

'''
Description - This functions runs the given cpp file for a given input and checks it's output with the expected output
Parameters -
	compiler - CPPCompiler - Runs the file for the input and returns the output.
	testCaseNo - int - Test Case number.
	input - string - input of the program.
	expectedOutput - string - expected output of the program.
Returns - 
	1 - If the expected output is same as the actual output.
	0 - If the expected output is different from actual output.
   -1 - If no expected output is provided.
   -2 - Runtime error. or any other problem during execution (Not TLE though).
'''
def runAndCheck(compiler , testCaseNo ,input = "" , expectedOutput = None):
	# Run and get the output of the program for the given input. Exception for runtime error.
	try:
		runOutput = compiler.run(input)
	except:
		return -2

	checkResult = None

	if not expectedOutput:
		expectedOutput = None

	runOutput = runOutput.strip()
	if expectedOutput: expectedOutput = expectedOutput.strip()

	if expectedOutput == None:
		checkResult = -1
	elif runOutput == expectedOutput:
		checkResult = 1
	else:
		checkResult = 0

	if checkResult == 0 or checkResult == -1:
		print("Input : ")
		print(input)

		if expectedOutput != None:
			expectedOutput = expectedOutput.strip()
			print("\nExpected Output : ")
			print(expectedOutput + "\n")

		runOutput = runOutput.strip()
		print("Actual Output : ")
		print(runOutput + "\n")
		
	return checkResult


'''
Description - This functions reads the data from a global input.txt files and returns it.
				If --add is at the beginning of the test case the adds it to the task data json file.
				If --output is presents then adds the expected output as well.
				If --testing test the given file with brute code and test case generator.
Parameters -
	None.
Returns - 
	inputData , outputData
'''
def getDataFromInputTxt():
	inputData = ''
	outputData = ''

	with open(inputTxtPath , 'rb') as inputFile:
		inputData = inputFile.read().decode();

	if '--add' in inputData:
		inputData = inputData[6:]
		if '--output' in inputData:
			inputData , outputData = inputData.split('--output') 
		task.addTask(inputData , outputData)

	if '--output' in inputData:
		inputData , outputData = inputData.strip().split('--output')

	return inputData , outputData



testNumber = 0
allOkCount = 0

inputData , outputData = getDataFromInputTxt()


tests = task.getTests()

# Add the data of global input.txt file to the testcases.
if inputData and {'input' : inputData , 'output' : outputData} not in tests:
	tests.append({'input' : inputData , 'output' : outputData})


# Check for each input/output.
for i_o in tests:
	print("Test Case : {}".format(testNumber))
	startTime = time.time()
	check_result = runAndCheck(compiler , testNumber , i_o['input'].strip() , i_o['output'])
	endTime = time.time()

	testNumber += 1
	print("Verdict :" , end = " ")
	if check_result == 1:
		allOkCount += 1
		print('AC ✔️')
	elif check_result == -1:
		allOkCount += 1
		print('Can\'t Say 🤷‍♂️')
	elif check_result == -2:
		print("RE ⚠️")
	else:
		print("WA ❌")

	print("Time Taken : " + str(round(endTime - startTime , 5)) + " s")
	print('-' * DASH_COUNT)



if testNumber == allOkCount:
	print("\nALL OK. 👍")
else:
	print("\nTesting Failed 👎")
