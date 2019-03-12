%{
	#include<bits/stdc++.h>
	using namespace std;
	int flag=1,pos=0;
	string input;
	stack<int> s;
%}

%%
[ab]+ {input=yytext;}
.		{flag=0;}
\n 		{return 0;}
%%

int yywrap();
int GOTO(int i,string s)
{
	if(i==0&&s=="S")return 1;
	if(i==0&&s=="A")return 2;
	if(i==2&&s=="A")return 5;
	if(i==3&&s=="A")return 6;
}
string ACTION(int i,string s)
{
	if(i==0&&s=="a")return "s3";
	if(i==0&&s=="b")return "s4";
	if(i==1)return "accept";
	if(i==2&&s=="a")return "s3";
	if(i==2&&s=="b")return "s4";
	if(i==3&&s=="a")return "s3";
	if(i==3&&s=="b")return "s4";
	if(i==4)return "r3";
	if(i==5&&s=="$")return "r1";
	if(i==6)return "r2";
}
void display()
{
	stack<int> tmp;
	while(!s.empty())
	{
		cout<<s.top()<<" ";
		tmp.push(s.top());
		s.pop();
	}
	while(!tmp.empty())
	{
		s.push(tmp.top());
		tmp.pop();
	}
	cout<<endl;
}
main()
{
	yylex();
	input = input+"$";
	if(flag)
	{
		s.push(0);
		while(1)
		{
			display();
			int u=s.top();
			string res=ACTION(u,input.substr(pos,1));
			if(res=="s3")
			{
				s.push(3);
				pos++;
			}
			else if(res=="s4")
			{
				s.push(4);
				pos++;
			}
			else if(res=="s5")
			{
				s.push(5);
				pos++;
			}
			else if(res=="r1")
			{
				s.pop();
				s.pop();
				u=s.top();
				s.push(GOTO(u,"S"));
			}
			else if(res=="r2")
			{
				s.pop();
				s.pop();
				u=s.top();
				s.push(GOTO(u,"A"));
			}
			else if(res=="r3")
			{
				s.pop();
				u=s.top();
				s.push(GOTO(u,"A"));
			}
			else if(res=="accept")
			{
				printf("accepted\n");
				exit(0);
			}
			else
			{
				printf("rejected\n");
				exit(0);
			}
		}
	}
}