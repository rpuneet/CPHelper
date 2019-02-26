import os , subprocess

TIMEOUT = 3

class CPPCompiler:

	def __init__(self , basePath):
		self.basePath = basePath
		self.cppFilePath = ''.join((basePath , '.cpp'))
		self.outputFile = basePath

	def compile(self):
		compileCommand = "g++ {} -o {}".format(self.cppFilePath , self.outputFile)
		compileCommand = compileCommand.split(' ')
		output = subprocess.check_output(compileCommand)
		return output

	def run(self , input):
		read, write = os.pipe()
		os.write(write, input)
		os.close(write)

		runCommand = "{}".format(self.outputFile)
		runCommand.split(' ')
		output = subprocess.check_output(runCommand, stdin=read)
		return output