#include<bits/stdc++.h>
using namespace std;
char input[100];
char prod[100][100];
int pos=-1,l,st=-1,flag=1;
char id,num;
int E();
int T();
int F();
void advance();
int Td();
int Ed();
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
int E()
{
	int e,t,ed;
	t=T();
	ed=Ed();
	e = t + ed;
	cout<<"E -> "<<t << " + "<<ed<<endl;
	return e;
}
int Ed()
{
	if(input[pos]=='+')
	{
		int t,ed,res;
		advance();
		t=T();
		ed=Ed();
		res = t + ed;
		cout<<"Ed -> "<<t << " + "<<ed<<endl;
		return res;
	}
	cout<<"Ed -> "<<0<<endl;
	return 0;
}

int T()
{
	int t,f,td;
	f=F();
	td=Td();
	t = f * td;
	cout<<"T -> "<<f << " * "<<td<<endl;
	return t;
}
int Td()
{
	if(input[pos]=='*')
	{
		int f,td,res;
		advance();
		f=F();
		td=Td();
		res = f * td;
		cout<<"Td -> "<<f << " * "<<td<<endl;
		return res;
	}
	cout<<"Td -> "<<1<<endl;
	return 1;
}
int F()
{
	int p=1;
	if(input[pos]=='(')
	{p=0;
		int e;
		advance();
		e=E();
		cout<<"F-> "<<e<<endl;
		if(input[pos]==')')   {
		advance();   
		return e;     
	   }
	}
	if(input[pos]==num)
	{p=0;
		cout<<"F-> "<<num<<endl;
		advance();
		return num-'0';
		
	}
	if(p==1)
		flag=0;
}
int main()
{
	int i,e;
	printf("Enter Input String :\n");
	scanf("%s",input);
	l=strlen(input);
	input[l]='$';
	advance();
	e=E();
	if(pos==l and flag)
	{
		printf("String Accepted\n");
		cout<<"Ans = "<<e<<endl;
	}
	else
	{
		printf("String rejected\n");
	}
	return 0;
}