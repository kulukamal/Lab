%{
	int side=0;
	int flag=0;
	char s;
	char rule[100];
	char input[100],*l,*r,*temp,tempprod[20],productions[25][50];
%}

%%

end			{return 0;}
->			{side=1;}
[A-Za-z]+	{
				if(side)
					r=yytext;
				else
					l=yytext;
			}
\n 			{return 0;}
%%
int yywrap(){}

int main()  {
    
    int i=0,j=0,flag=0;
    l = strtok(input,"->");
    r = strtok(NULL,"->");
    temp = strtok(r,"|");
    while(temp)  {
        if(temp[0] == l[0])  {
            flag = 1;
            sprintf(productions[i++],"%s'->%s%s'\0",l,temp+1,l);
        }
        else
            sprintf(productions[i++],"%s->%s%s'\0",l,temp,l);
        temp = strtok(NULL,"|");
    }
    sprintf(productions[i++],"%s'->^",l);
    if(flag == 0)
        printf("The given productions don't have Left Recursion");
    else
        for(j=0;j<i;j++)  {
            printf("\n%s",productions[j]);
        }
     printf("\n");
}
