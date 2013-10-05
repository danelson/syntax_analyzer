#!/usr/bin/python
# -*- coding: utf-8 -*-

# Daniel Nelson
# https://github.com/danelson
# abstract.py

import token


#==== Program =======================================================

class Program:
	'''
	Responsible for printing the program header and calling any of its nodes in
	the tree.
	'''
	
	def __init__(self, decpart=None, body=None):
		'''
		Initializes the Program class with a decpart and a body
		@decpart: a list of declarations
		@body: a list of statements
		'''
		self.decpart = decpart
		self.body = body
		
		
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}Program".format(indent)
	
		print "{0}  |-Declarations".format(indent)
		for decl in self.decpart:
			decl.printTree(indent)
	
		print "{0}  |-Statements".format(indent)
		for stmt in self.body:
			stmt.printTree(indent + "  |  ")
			
#====================================================================


#==== Declarations ==================================================

class Declarations:
	'''
	Responsible for printing the declarations header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, decl=None):
		'''
		Initializes the Declaration class with a variable and a vartype
		@decl: a list of declartion
		'''
		self.decl = decl
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		for dec in self.decl:
			dec.printTree(indent + "  |  ")

#====================================================================


#==== Declaration ===================================================

class Declaration:
	'''
	Responsible for printing the declaration header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, variable=None, type=None):
		'''
		Initializes the Declaration class with a variable and a vartype
		@variable: a string
		@vartype: a string
		'''
		self.type = type
		self.variable = variable
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Declaration".format(indent)
		self.type.printTree(indent + "|  ")
		self.variable.printTree(indent + "|  ")

#====================================================================


#==== Statements ====================================================

class Statements:
	'''
	Responsible for printing the statements header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, states=None):
		'''
		Initializes the Statement class to either an int or float
		@states: a list of states
		'''
		self.states = states
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		for state in self.states:
			state.printTree(indent)
			
#====================================================================


#==== Statement =====================================================

class Statement:
	'''
	Responsible for printing the statement header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, expr=None, body=None):
		'''
		Initializes the Statement class to either an int or float
		@type: a list of assignments or conditionals
		'''
		self.expr = expr
		self.body = body
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		'''
		if self.body != None:
			for item in self.body:
				item.printTree(indent + "|  ")
		self.expr.printTree(indent + "|  ")
		'''

		print "{0}|-While Statement".format(indent)
		self.expr.printTree(indent + "|  ")
		for item in self.body:
			item.printTree(indent + "|  ")		
			
#====================================================================


#==== Assignment ====================================================

class Assignment:
	'''
	Responsible for printing the assignment header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, target=None, source=None):
		'''
		Initializes the Assignment class
		@target: an identifier
		@source: an expression
		'''
		self.target = target
		self.source = source
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Assignment".format(indent)
		self.target.printTree(indent + "|  ")
		self.source.printTree(indent + "|  ")

#====================================================================


#==== Conditional ===================================================
		
class Conditional:
	'''
	Responsible for printing the conditional header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, target=None, source=None):
		'''
		Initializes the Conditional class
		@target: an if or else statment
		@source: body of the conditional
		'''
		self.target = target
		self.source = source
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-If Statement".format(indent)
		self.target.printTree(indent + "|  ")
		for item in self.source:
			item.printTree(indent + "|  ")

#====================================================================


#==== Ifstatement ===================================================
		
class Ifstatement:
	'''
	Responsible for printing the if statement header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, comp=None):
		'''
		Initializes the Conditional class
		@comp: a comparison
		'''
		self.comp = comp
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		for item in self.comp:
			item.printTree(indent)		

#====================================================================


#==== Elsestatement =================================================
		
class Elsestatement:
	'''
	Responsible for printing the else statment header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, body=None):
		'''
		Initializes the Conditional class
		@body: body of the conditional
		'''
		self.body = body
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		# Correct the positioning of the string
		newIndent = indent[0:len(indent)-2]
		print "{0}-Else Statement".format(newIndent)
		for item in self.body:
			item.printTree(indent)		

#====================================================================


#==== Whilestatement ================================================
		
class Whilestatement:
	'''
	Responsible for printing the while statement header and calling any of
	its nodes in the tree.
	'''
	
	def __init__(self, expr=None, body=None):
		'''
		Initializes the Conditional class
		@expr: the test of the while
		@body: the body of the body
		'''
		self.expr = expr
		self.body = body
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		if self.body != None:
			for item in self.body:
				item.printTree(indent + "|  ")
		if self.expr != None:
			for item in self.expr:
				item.printTree(indent)
		

#====================================================================


#==== Equality ======================================================
		
class Equality:
	'''
	Responsible calling any of its nodes in the tree.
	'''
	
	def __init__(self, expr=None):
		'''
		Initializes the Equality class
		@expr: an expression
		'''
		self.expr = expr
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		self.expr.printTree(indent)		

#====================================================================


#==== Comparison ====================================================

class Comparison:
	'''
	Comparison
	'''
	def __init__(self, op=None):
		'''
		Initializes the Variable class
		@op: The comparison operation
		'''
		self.op = op
	
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Comparison".format(indent) + " : " + self.op.value
		
#====================================================================	


#==== Variable ======================================================
		
class Variable:
	'''
	Variable
	'''
	
	def __init__(self, var=None):
		'''
		Initializes the Variable class
		@var: the variable
		'''
		self.var = var
		
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		# Check if it is a token object
		if isinstance(self.var,token.Token):
			print "{0}|-Variable".format(indent) + " : " + self.var.value
		# Otherwise move down the tree
		else:
			for item in self.var:
				print 'test'
				item.printTree(indent + "  |  ")
		
#====================================================================


#==== Binary ========================================================

class Binary:
	'''
	Binary
	'''
	
	def __init__(self, op=None, term1=None, term2=None):
		'''
		Initializes the Binary class
		@op: the operation
		@term1: the first term
		@term2: the second term
		'''
		self.op = op
		self.term1 = term1
		self.term2 = term2
		
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Binary".format(indent)
		self.op.printTree(indent + "|  ")
		self.term1.printTree(indent + "|  ")
		self.term2.printTree(indent + "|  ")
		
#====================================================================


#==== Unary =========================================================

class Unary:
	'''
	Unary
	'''
	
	def __init__(self, op=None, term=None):
		'''
		Initializes the Binary class
		@op: the operation
		@term: the term
		'''
		self.op = op
		self.term = term
		
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Unary".format(indent)
		self.op.printTree(indent + "|  ")
		self.term.printTree(indent + "|  ")
		
		
#====================================================================


#==== Operator ======================================================

class Operator:
	'''
	Operator
	'''
	
	def __init__(self, op=None):
		'''
		Initializes the Operator class
		@op: an operation
		'''
		self.op = op
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Operator".format(indent) + " : " + self.op.value

#====================================================================


#==== Type ==========================================================

class Type:
	'''
	Type
	'''
	
	def __init__(self, type=None):
		'''
		Initializes the Type class
		@type: the type of a variable (int or float)
		'''
		self.type = type
		
			
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Type".format(indent)  + " : " + self.type.value

#====================================================================


#==== Literal =======================================================

class Literal:
	'''
	Literal
	'''
	
	def __init__(self, lit=None):
		'''
		Initializes the Literal class
		@lit: a literal object (int or float)
		'''
		self.lit = lit

	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		self.lit.printTree(indent) 
		
		
#====================================================================	


#==== Integer =======================================================

class Integer:
	'''
	Integer
	'''
	def __init__(self, val=None):
		'''
		Initializes the Variable class
		@val: The token holding the ints value
		'''
		self.val = val
	
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Integer".format(indent) + " : " + self.val.value

#===================================================================


#==== Float =========================================================

class Float:
	'''
	Float
	'''
	def __init__(self, val=None):
		'''
		Initializes the Variable class
		@val: The token holding the floats val
		'''
		self.val = val
		
	def printTree(self, indent):
		'''
		Prints the components of the abstract class
		@indent: the formatting for indentation
		'''
		print "{0}|-Float".format(indent) + " : " + self.val.value

#====================================================================	





#=== TEST ==========================================================
		
if __name__ == "__main__":
	print 'test'
	
	