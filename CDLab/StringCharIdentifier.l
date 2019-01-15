%{
	int flag=1,Char=0,String=0;
%}
letter [a-zA-Z0-9!@#$%^&*()_+-=]
%%
"'"{letter}"'" 		{Char = 1;}
"\""({letter}*)"\""	{String = 1;}
.					{}
\n					{return 0;}
%%

int yywrap(){}

int main()
{
	yylex();

	if(Char == 1)
		printf("Character !!\n");
	else if(String == 1)
		printf("String !!\n");
	else
		printf("Not a Character or String !!\n");
}