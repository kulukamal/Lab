#include<bits/stdc++.h>
using namespace std;
char input[100];
char prod[100][100];
int pos=-1,l,st=-1,flag=1;
char id,num;
void E();
void T();
void F();
void advance();
void Td();
void Ed();
void advance()
{
	pos++;
	if(pos<l)
	{
		if(input[pos]>='0'&& input[pos]<='9')
		{
			num=input[pos];
			id='\0';
		}
		if((input[pos]>='a' || input[pos]>='A')&&(input[pos]<='z' || input[pos]<='Z'))
		{
			id=input[pos];
			num='\0';
		}
	}
}
void E()
{
	T();
	Ed();
}
void Ed()
{
	int p=1;
	if(input[pos]=='+')
	{
		p=0;
		advance();
		T();
		Ed();
	}
	if(input[pos]=='-')
	{   
		p=0;
		advance();
		T();
		Ed();
	}
}

void T()
{
	F();
	Td();
}
void Td()
{
	int p=1;
	if(input[pos]=='*')
	{
		p=0;
		advance();
		F();
		Td();
	}
	if(input[pos]=='/')
	{   p=0;
		advance();
		F();
		Td();
	}
}
void F()
{
	int p=1;
	if(input[pos]==id) {p=0;
		advance();        
	  }
	if(input[pos]=='(')
	{p=0;
		advance();
		E();
		if(input[pos]==')')   {
		advance();        
	   }
	}
	if(input[pos]==num)
	{p=0;
		advance();
	}
	if(p==1)
		flag=0;
}
int main()
{
	int i;
	printf("Enter Input String ");
	scanf("%s",input);
	l=strlen(input);
	input[l]='$';
	advance();
	E();
	if(pos==l and flag)
	{
		printf("String Accepted\n");
		for(i=0;i<=st;i++)
		{
			printf("%s\n",prod[i]);
		}
	}
	else
	{
		printf("String rejected\n");
	}
	return 0;
}