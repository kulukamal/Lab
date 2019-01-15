%{
	int opeartor=0;
	float a,b;
%}

%%
[0-9]+|([0-9]*)"."([0-9]+) {StringToDigit();} 
"+" {opeartor=1;}
"-" {opeartor=2;}
"*" {opeartor=3;}
"/" {opeartor=4;}
[ \t]* {}
.	{printf("No valid Inputs!!");return 0;}
\n {return 0;}

%%

StringToDigit()
{
	if(opeartor==0)
	a=atof(yytext);
	else
	{
		b=atof(yytext);
		switch(opeartor)
		{
			case 1:a=a+b;
			break;
			case 2:a=a-b;
			break;
			case 3:a=a*b;
			break;
			case 4:a=a/b;
			break;
		}
		opeartor=0;
	}
}
int yywrap(){}
main()
{
	yylex();
	if(!opeartor)
	printf("Ans = %f\n",a);
}

