%{
	#include<string.h>
	char *Table[1000];
	int i=0,j;
%}

digit       [0-9]
ichar       [A-Z_a-z]
integer     {digit}+
identifier  {ichar}([0-9]|{ichar})*
float       ([+-]?{digit}+)?\.{digit}*(e?[+-]?{digit}+)?
chrliteral  "'"(\\?[^"'])"'"
escquote    [^"]*\\\"[^"]*
strliteral  \"[^"]*{escquote}*\"

%%
"end"			{
				  return 0;
				}

"if"            { printf("if\t::\tkey word\n");}
"else"          { printf("else\t::\tkey word\n");}
"while"         { printf("while\t::\tkey word\n");}
"return"        { printf("return\t::\tkey word\n");}
"break"         { printf("break\t::\tkey word\n");}
"goto"          { printf("goto\t::\tkey word\n");}
"float"         { printf("float\t::\tkey word\n");}
"int"           { printf("int\t::\tkey word\n");}
"void"          { printf("void\t::\tkey word\n");}
"char"          { printf("char\t::\tkey word\n");}

"="             { printf("=\t::\toperator\n");}
"!="            { printf("!=\t::\toperator\n");}
"=="            { printf("==\t::\toperator\n");}
"<"             { printf("<\t::\toperator\n");}
"<="            { printf("<=\t::\toperator\n");}
">"             { printf(">\t::\toperator\n");}
">="            { printf(">=\t::\toperator\n");}
"&&"            { printf("&&\t::\toperator\n");}
"||"            { printf("||\t::\toperator\n");}



"+"             { printf("+\t::\toperator\n");}
"-"             { printf("-\t::\toperator\n");}
"*"             { printf("*\t::\toperator\n");}
"/"             { printf("/\t::\toperator\n");}
"%"             { printf("%\t::\toperator\n");}
","             { printf(",\t::\toperator\n");}


"{"             { printf("{\t::\tpunctuator\n");}
"}"             { printf("}\t::\tpunctuator\n");}
"["             { printf("[\t::\tpunctuator\n");}
"]"             { printf("]\t::\tpunctuator\n");}
"("             { printf("(\t::\tpunctuator\n");}
")"             { printf(")\t::\tpunctuator\n");}
";"             { printf(";\t::\tpunctuator\n");}

{float}         { 
                  printf("%s\t::\tFloat Literal\n",yytext);
                }

{integer}       { 
                  printf("%s\t::\tInt Literal\n",yytext);
                }

{chrliteral}    { 
                  printf("%s\t::\tChar Literal\n",yytext);
                }

{strliteral}    { 
                  printf("%s\t::\tString Literal\n",yytext);
                }

{identifier}    { 
                  printf("%s\t::\tIdentifier\n",yytext);
                }

\n				{}
.				{}



%%
void foo(char *str)
{
	if(i==0)
	{
		Table[i] = malloc(sizeof(str));
		Table[i] = str;
		i++;
	}
	else
	{
		for(j=0;j<=i;j++)
		{
			if(!strcmp(Table[j],str))
			{
				return;
			}
		}
		Table[i] = malloc(sizeof(str));
		Table[i] = str;
		i++;
	}
}
int yywrap(){}

main()
{
	yylex();

}

