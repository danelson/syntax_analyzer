# Dan Nelson
# CS333
# Project 3
# lexer.py
# October 13, 2011

import token

class Lexer:
	'''
	The lexer class creates tokens from a text file generated by our
	lexical analyzer in project 2.
	'''
	
	def __init__(self, file=None):
		'''
		Initializes the Lexer class with a file
		@file: the file to read from
		'''
		self.lineNum = 1
		self.token = None
		self.lineTest = False
		if file != None:
			self.file = open(file,'r')
		self.nextToken()
		
		
	def nextToken(self):
		'''
		Reads the next line from a file and splits it based on the first
		'-'	character. It builds a token object from its type and value.
		When we reach the end of the file create a special token object.
		'''
		line = self.file.readline()
		line = line.strip("\n")
		self.lineTest = False
		
		#get rid of all the newline tokens
		while line == "Newline":
			self.lineTest = True
			self.lineNum += 1
			line = self.file.readline()
			line = line.strip("\n")
		info = line.split('-',1)
		
		# Create a token with the proper fields
		if (len(info) > 1):
			self.token = token.Token(info[0], info[1])
		elif (len(info) == 1):
			self.token = token.Token(info[0])
		
		# create a special token object
		if len(line) < 2:
			self.token = token.Token("END")
	
	
	def currToken(self):
		'''
		Returns the current token object
		'''
		return self.token
		
		
		
if __name__ == "__main__":
	lexer = Lexer("test.txt")
	lexer.nextToken()
	lexer.nextToken()
	lexer.nextToken()
	lexer.nextToken()
	lexer.nextToken()
	
	
	
		