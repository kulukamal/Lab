%{
	int flag=1;
	int len=0;
%}

%%

[a-zA-Z_]	{
				len++;
			}
[0-9]		{
				len++;
				if(len==1)
				flag=0;
			}
. 			{flag=0;}
\n			{return 0;}
%%

int yywrap(){}
int main()
{
	yylex();
	if(flag)
		printf("accepted\n");
	else
		printf("rejected\n");
}