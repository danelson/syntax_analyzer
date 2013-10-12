README.txt

To create an abstract syntax tree for a Clite program do the following:

Place a Clite file in the same directory as the lexical and syntactic analyzers

Create a file of tokens using our lexical analyzer:

$ flex clite.yy 
$ gcc -o cli lex.yy.c -lfl

For this line include the <> brackets
$ ./cli <filename> destination.txt

Create the abstract syntax tree based on the tokens:

$ python parser.py <filename>


The write-up for this week's project can be found at:

http://web.colby.edu/danelson/2011/10/17/project-3-syntax-analysis/