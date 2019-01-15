%{
	int prv=0;
	int flag=1,Open=0,Close=0,op1=0,op2=0;
%}

%%

[a-zA-Z0-9]+	{
				op1++;
				if(prv==1)
					{
						flag=0;
						return 0;
					}
				prv=1;
				}

[-+\*]			{
					op2++;
					if(prv==0 || prv==2)
					{
						flag=0;
						return 0;
					}
					prv=0;
				}
"("			{
				prv=2;
				if(Close<=Open)Open++;

			}
")"			{
				if(prv==0)
					{
						flag=0;
						return 0;
					}
				prv=2;
				Close++;
			}
[ \t]*		{}
.			{flag=0;return 0;}
\n			{return 0;}

%%

int yywrap(){}

main()
{
	yylex();
	printf("%d : %d : %d : %d\n",Open,Close,op1,op2);
	if(flag && Open==Close && op1>op2)
		printf("accepted\n");
	else
		printf("rejected\n");

}