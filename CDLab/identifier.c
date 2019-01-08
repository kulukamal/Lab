#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char const *argv[])
{
	char str[80];
	int flag=1,ascVal,i;
	scanf("%[^\n]",str);

	for(i=0;i<strlen(str) && flag;++i)
	{
		ascVal = (int)str[i];
		if(i==0)
		{
			if(!(ascVal == 95 || ascVal >= 65 && ascVal <=90 || ascVal>=97 && ascVal<=122))
				flag=0;
		}
		else
		{
			if(!(ascVal == 95 || ascVal >= 65 && ascVal <=90 || ascVal>=97 && ascVal<=122||ascVal>=48 && ascVal<=57))
				flag=0;
		}
	}
	if(flag)
		printf("valid\n");
	else
		printf("invalid\n");
	return 0;
}