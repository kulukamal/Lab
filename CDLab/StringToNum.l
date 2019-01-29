%{
	int val=0;
%}



%%
[0-9]+	 	{ToInt();}
"one"	{StringToInt(1);}
"two"	{StringToInt(2);}
"three"	{StringToInt(3);}
"four"	{StringToInt(4);}
"five"	{StringToInt(5);}
"six"	{StringToInt(6);}
"seven"	{StringToInt(7);}
"eight"	{StringToInt(8);}
"nine"	{StringToInt(9);}
"ten"	{StringToInt(10);}

"eleven" {StringToInt(11);}
"tweleve"{StringToInt(12);}
"thirteen"{StringToInt(13);}
"fourteen"
%%


int yywrap(){}

main()
{
	yylex();

}


