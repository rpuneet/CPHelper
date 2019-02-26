from CPPCompiler import CPPCompiler
from Task import Task
import sys


BASE_PATH = sys.argv[1]

compiler = CPPCompiler(BASE_PATH)
task = Task(BASE_PATH)

try:
	compileOutput = compiler.compile()
except:
	print "Compilation Error"
	sys.exit(0)


def runAndCheck(compiler , testCaseNo ,input = "" , expectedOutput = None):
	try:
		runOutput = compiler.run(input)
	except:
		print "\nRuntime Error"
		sys.exit(0)

	print "Test Case #%s : \nInput : " %testCaseNo
	print input
	if expectedOutput != None:
		print "\nExpected Output : "
		expectedOutput = expectedOutput.strip()
		print expectedOutput + "\n"
	print "Actual Output : "
	runOutput = runOutput.strip()
	print runOutput + "\n"
	if expectedOutput == None:
		return True
	if runOutput == expectedOutput:
		return True
	else:
		return False




testNumber = 0
allOkCount = 0
tests = task.getTests()
for i_o in tests:
	check_result = runAndCheck(compiler , testNumber , i_o['input'] , i_o['output'])
	testNumber += 1
	if check_result:
		allOkCount += 1
		print 'Success!'
	else:
		print "Wrong Answer" 
	print '-' * 20


inputData = ''

with open("/home/schitzo/Documents/Programming/input.txt" , 'rb') as inputFile:
	inputData = inputFile.read();

if inputData:
	runAndCheck(compiler , testNumber , inputData)
	testNumber += 1
	allOkCount += 1

if testNumber == allOkCount:
	print "\nALL OK"
else:
	print "\nSome test cases Failed"