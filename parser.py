#!/usr/bin/python
# -*- coding: utf-8 -*-

# Daniel Nelson
# https://github.com/danelson
# parser.py

import sys
import lexer
import token
import abstract

class Parser:
	'''
	Parser
	'''
	
	def __init__(self, file):
		'''
		Initializes the Parser class
		@file: the file to read in
		'''
		self.lexer = lexer.Lexer(file)
		self.file = file
		
	
	def parse(self, indent):
		'''
		Runs the parser
		@indent: the starting indentation for the output
		'''
		program = self.program()
		program.printTree("")
		print "End"
	
	
	def match(self, token):
		'''
		Compares a token to the current token from the Lexer. If the
		tokens match in type, it advances the Lexer to the next token.
		If it does not match, it calls the error method.
		@token: the token to compare with the lexer's current token
		@return: If no error is produced, it returns the value of the
				 matched token.
		'''
		ret = self.lexer.currToken()
		val = token.compare(ret)
		if val > 0:
			self.lexer.nextToken()
			return ret
		else:
			self.error(token, val)
			
	
	def matchBoth(self, token):
		'''
		Compares a token to the current token from the Lexer. If the
		tokens match in both value and type, it advances the Lexer 
		to the next token. If it does not match, it calls the error
		method.
		@token: the token to compare with the lexer's current token
		@return: If no error is produced, it returns the value of the
				 matched token.
		'''
		ret = self.lexer.currToken()
		val = token.compare(ret)
		if val == 2:
			self.lexer.nextToken()
			return ret
		else:
			self.error(token, val)
		
		
	def error(self, token, error):
		'''
		Accepts a token parameter and prints an	error message indicating
		that the Parser expected expected a different token. It then
		terminates the program.
		@token: the token that was expected
		@value: the error message
		'''
		# Find the actual line number
		lineNum = self.lexer.lineNum
		if self.lexer.lineTest:
			lineNum -= 1
		
		if error == 0:
			print "  File '" + self.file + "', line " + str(lineNum)
			print "    TypeError: Expected '" + str(token.type) + \
					"' but saw '" + str(self.lexer.currToken().type) + "'"
		else:
			print "  File '" + self.file + "', line " + str(lineNum)
			print "    ValueError: Expected '" + str(token.value) + \
					"' but saw '" + str(self.lexer.currToken().value) + "'"
		sys.exit()
		
		
	def anyOf(self, tokens):
		'''
		Accepts a list of tokens and returns true if the list contains
		a token of the same type as the current token. This is helpful
		for checking if the current	token matches any of the type names
		(e.g. for processing all declarations) or any of a set of operators.
		@tokens: a list of tokens for comparison
		@return: True if the tokens contains a token of the same type as
				 the current token
		'''
		for token in tokens:
			if token.compare(self.lexer.currToken()) == 2:
				return 2
			elif token.compare(self.lexer.currToken()) == 1:
				return 1
		return 0
		
		
	def program(self):
		'''
		Concrete syntax:
		int main () { Declarations Statements }
		@return: a Program object
		'''
		# Static for beginning of file
		self.matchBoth(token.Token("Keyword", "int"))
		self.matchBoth(token.Token("Identifier", "main"))
		self.matchBoth(token.Token("Open", "paren"))
		self.matchBoth(token.Token("Close", "paren"))
		self.matchBoth(token.Token("Open", "bracket"))
		program = abstract.Program(self.declarations(), self.statements())
		self.matchBoth(token.Token("Close", "bracket"))
		self.match(token.Token("END"))
		return program
		
		
	def declarations(self):
		'''
		Concrete syntax:
		{ Declaration }
		@return: a list of Declarations objects
		'''
		declslist = []
		while self.anyOf([token.Token("Keyword","int"),token.Token("Keyword","float")]):
			declslist.append(abstract.Declarations(self.declaration()))
		return declslist
		
		
	def declaration(self):
		'''
		Concrete syntax:
		Type Identifier {, Identifier};
		@return: a list of Declaration objects
		'''
		declist = []
		vartype = abstract.Type(self.match(token.Token("Keyword")))
		var = abstract.Variable(self.match(token.Token("Identifier")))
		declist.append(abstract.Declaration(var,vartype))
		
		# Multiple declarations on the same line
		while self.anyOf([token.Token("Comma")]):
			self.lexer.nextToken()
			var = abstract.Variable(self.match(token.Token("Identifier")))
			declist.append(abstract.Declaration(var,vartype))
		self.match(token.Token("Semicolon"))
		return declist
		
		
	def statements(self):
		'''
		Concrete syntax:
		{ Statement }
		@return: a list of statements objects
		'''
		stateslist = []
		while self.anyOf([token.Token("Identifier"), token.Token("Keyword")]):
			stateslist.append(abstract.Statements(self.statement()))
		return stateslist
		
		
	def statement(self):
		'''
		Concrete syntax:
		Assignment | IfStatement
		@return: a list of Conditional and Assignment objects
		'''
		statelist = []
		while self.anyOf([token.Token("Keyword"), token.Token("Identifier")]):
			if self.anyOf([token.Token("Keyword")]):
				# If we have an if statement
				if self.lexer.currToken().value == "if":
					ifState = self.ifStatement()
					statelist.append(abstract.Conditional(ifState[0],ifState[1]))
				# If we have a while statement
				elif self.lexer.currToken().value == "while":
					whileState = self.whileStatement()
					statelist.append(abstract.Statement(whileState[0],whileState[1]))					
			# If we have an assignment
			elif self.anyOf([token.Token("Identifier")]):
				assign = self.assignment()
				statelist.append(abstract.Assignment(assign[0],assign[1]))
		return statelist
		
		
	def assignment(self):
		'''
		Concrete syntax:
		Identifier = Expression;
		@return: a list of a Variable object and an Equality object
		'''
		target = abstract.Variable(self.match(token.Token("Identifier")))
		self.match(token.Token("Assignment"))
		source = abstract.Equality(self.expression())
		self.match(token.Token("Semicolon"))
		return [target,source]
		
		
	def ifStatement(self):
		'''
		Concrete syntax:
		if ( Expression ) Statement [ else Statement ]
		@return: a list of an Equality object and a list of Conditonal Objects
		'''
		conditional = []
		var = abstract.Variable(self.match(token.Token("Keyword", "if")))
		expr = abstract.Equality(self.expression())
		self.matchBoth(token.Token("Open", "bracket"))
		conditional.append(abstract.Ifstatement(self.statement()))
		self.matchBoth(token.Token("Close","bracket"))
		
		# If we encounter an 'else' statement after an 'if'
		if self.anyOf( [token.Token("Keyword","else")] ):
			self.matchBoth(token.Token("Keyword", "else"))
			self.matchBoth(token.Token("Open", "bracket"))
			conditional.append(abstract.Elsestatement(self.statement()))
			self.matchBoth(token.Token("Close","bracket"))
		return [expr, conditional]
		
	
	def whileStatement(self):
		'''
		Concrete syntax:
		while ( Expression ) Statement
		'''
		loop = []
		var = abstract.Variable(self.matchBoth(token.Token("Keyword", "while")))
		expr = abstract.Equality(self.expression())
		self.matchBoth(token.Token("Open", "bracket"))
		loop.append(abstract.Whilestatement(self.statement()))
		self.matchBoth(token.Token("Close","bracket"))
		return [expr, loop]
		
		
	def expression(self):
		'''
		In case I implement more of Clite
		Currently just passing down the tree
		'''
		return self.equality()
		
	
	def equality(self):
		'''
		Concrete syntax:
		Additon [EquOp Addition]
		@return: either a return value from down the tree or a Binary
				 object
		'''
		addition = self.addition()
		
		# If we have a comparison
		if self.anyOf([token.Token("Comparison", "=="), token.Token("Comparison", "!=")]) == 2:
			comp = abstract.Comparison(self.match(token.Token("Comparison")))
			addition2 = self.addition()
			addition = abstract.Binary(comp,addition,addition2)
		return addition
				
			
	def addition(self):
		'''
		Concrete syntax:
		Term { AddOp Term }
		@return: either a return value from down the tree or a Binary
				 object
		'''
		term = self.term()
		while self.anyOf([token.Token("Operator", "+"), token.Token("Operator", "-")]) == 2:
			op = abstract.Operator(self.match(token.Token("Operator")))
			term2 = self.term()
			term = abstract.Binary(op,term,term2)
		return term
		
		
	def term(self):
		'''
		Concrete syntax:
		Factor { MulOp Factor }
		@return: either a return value from down the tree or a Binary
				 object
		'''
		factor = self.factor()
		while self.anyOf([token.Token("Operator", "*"), token.Token("Operator", "/")]) == 2:
			op = abstract.Operator(self.match(token.Token("Operator")))
			factor2 = self.factor()
			factor = abstract.Binary(op, factor, factor2)
		return factor
		
		
	def factor(self):
		'''
		Concrete syntax:
		[ UnaryOp ] Primary
		@return: either a Unary object or a return value from down the tree
				 object
		'''
		if self.anyOf([token.Token("Operator", "-"), token.Token("Operator", "!")]) == 2:
			op = abstract.Operator(self.match(token.Token("Operator")))
			primary = self.primary()
			primary = abstract.Unary(op,primary)
		else:
			primary = self.primary()
		return primary
		
		
	def primary(self):
		'''
		Concrete syntax:
		Identifier | Literal | (Expression)
		@return: a Variable object, a Literal object, or another return value
				 that goes back down the tree
		'''
		if self.anyOf([token.Token("Identifier")]):
			expr = abstract.Variable(self.match(token.Token("Identifier")))
		elif self.anyOf([token.Token("Integer"),token.Token("Float")]):
			expr = abstract.Literal(self.literal())
		else:
			self.matchBoth(token.Token("Open", "paren"))
			expr = self.expression()
			self.matchBoth(token.Token("Close", "paren"))
		return expr
		
		
	def literal(self):
		'''
		Concrete syntax:
		Integer | Float
		@return: an Integer object or a Float object
		'''
		if self.anyOf([token.Token("Integer")]):
			source = abstract.Integer(self.match(token.Token("Integer")))
		elif self.anyOf([token.Token("Float")]):
			source = abstract.Float(self.match(token.Token("Float")))
		return source
		
		

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "  Usage: parser.py <filename>"
		sys.exit()
	parser = Parser(sys.argv[1])
	parser.parse("")
	
	
	
	
	
	
	