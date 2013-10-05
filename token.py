# Dan Nelson
# CS333
# Project 3
# token.py
# October 13, 2011


class Token:
	'''
	The Token class holds the type and value of each token from a Clite file.
	'''
	
	def __init__(self, type=None, value=None):
		'''
		Initializes the Token class with a type and a value
		@type: a string  (e.g. Identifier) 
		@value: a string (e.g. xyz)
		'''
		self.type = type
		self.value = value
		
		
	def printToken(self):
		'''
		Prints the token's type and value
		'''
		print "Type: " + self.type + "\tValue: " + self.value
		
		
	def compare(self, token):
		'''
		Compares 1 token against itself
		@token: the token to compare against
		@return: returns 2 if the tokens are the same type and value
				 returns 1 if the tokens are the same but the types are
					different
				 returns 0 if the tokens are not the same
		'''
		if self.type == token.type:
			if self.value == token.value:
				return 2
			return 1
		return 0
		
		
		
if __name__ == "__main__":
	token1 = Token("Variable", "int")
	token2 = Token("Variable", "float")
	token3 = Token("Variable", "int")
	token1.printToken()
	token2.printToken()
	token3.printToken()
	print token1.compare(token2)
	print token1.compare(token3)
	
	
	
	
		