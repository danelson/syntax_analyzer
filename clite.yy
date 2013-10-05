%{
/* Dan Nelson
 * Project 2
 * September 27, 2011
 * A flex file to parse clite.
 */
%}

Integer				{Digit}+
Float				{Integer}+\.{Integer}+
Keyword				(if|else|while|for|bool|char|int|float)
Identifier			[a-zA-Z_]+[a-zA-Z0-9_]*
Assignment			=
Comparison			(==|<|>|<=|>=)
Operator			(\+|-|\*|\/|%)
OpenBracket			\{
CloseBracket		\}
OpenParen			\(
CloseParen			\)
Semicolon			;
Digit				[0-9]
Space				\ +
EndLine				\n
Comma				\,
Tab					\t
Comment				\/\/.*

%%

{Comment}			{
	int length = strlen(yytext);
	char* words = yytext;
	char* out;
	strncpy(out,words+2,length);
	printf("Comment-%s\n", out);
}

{Integer}			{
	printf("Integer-%s\n", yytext);
}

{Float}				{
	printf("Float-%s\n", yytext);
}

{Keyword}			{
	printf("Keyword-%s\n", yytext);
}

{Identifier}		{
	printf("Identifier-%s\n", yytext);
}

{Assignment}		{
	printf("Assignment\n");
}

{Comparison}		{
	printf("Comparison-%s\n", yytext);
}

{Operator}			{
	printf("Operator-%s\n", yytext);
}

{OpenBracket}		{
	printf("Open-bracket\n");
}

{CloseBracket}		{
	printf("Close-bracket\n");
}

{OpenParen}			{
	printf("Open-paren\n");
}

{CloseParen}		{
	printf("Close-paren\n");
}

{Semicolon}			{
	printf("Semicolon\n");
}

{EndLine}			{
	printf("Newline\n");
}

{Comma}				{
	printf("Comma\n");
}

{Space}				{
}


{Tab}				{
}


%%

int main(int argc, char** argv) 
{
	yylex();
}