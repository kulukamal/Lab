%{
	int flag=1;
	int noOfZero=0,noOfOne=0;
%}

%%
[0] 	{noOfZero++;}
[1]		{noOfOne++;}
. 		{}
\n		{return 0;}
%%

int yywrap(){}
int main()
{
	yylex();
	if(noOfOne%2==1 || noOfZero%2==0)
		flag=0;
	if(flag)
		printf("accepted\n");
	else
		printf("rejected\n");
}