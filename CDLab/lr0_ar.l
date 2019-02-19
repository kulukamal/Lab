%{
   #include<bits/stdc++.h>
   using namespace std;
   int flag=1,pos=0;
   string input;
   stack<int> s;
%}

%%
[i+()]+ {input=yytext;}
.     {flag=0;}
\n       {return 0;}
%%

int yywrap();
int GOTO(int i,string s)
{
   if(i==0&&s=="E")return 1;
   if(i==0&&s=="T")return 9;
   if(i==3&&s=="T")return 4;
   if(i==6&&s=="E")return 7;
   if(i==6&&s=="T")return 9;
}
string ACTION(int i,string s)
{
   if(i==0&&s=="i")return "s5";
   if(i==0&&s=="(")return "s6";
   if(i==1&&s=="+")return "s3";
   if(i==1&&s=="$")return "s2";
   if(i==2)return "accept";
   if(i==3&&s=="i")return "s5";
   if(i==3&&s=="(")return "s6";
   if(i==4)return "r2";
   if(i==5)return "r4";
   if(i==6&&s=="i")return "s5";
   if(i==6&&s=="(")return "s6";
   if(i==7&&s==")")return "s8";
   if(i==7&&s=="+")return "s3";
   if(i==8)return "r5";
   if(i==9)return "r3";
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
         if(res=="s2")
         {
            s.push(2);
            pos++;
         }
         else if(res=="s3")
         {
            s.push(3);
            pos++;
         }
         else if(res=="s5")
         {
            s.push(5);
            pos++;
         }
         else if(res=="s6")
         {
            s.push(6);
            pos++;
         }
         else if(res=="s8")
         {
            s.push(8);
            pos++;
         }
         else if(res=="r2")
         {
            s.pop();
            s.pop();
            s.pop();
            u=s.top();
            s.push(GOTO(u,"E"));
         }
         else if(res=="r3")
         {
            s.pop();
            u=s.top();
            s.push(GOTO(u,"E"));
         }
         else if(res=="r4")
         {
            s.pop();
            u=s.top();
            s.push(GOTO(u,"T"));
         }
          else if(res=="r5")
         {
            s.pop();
            s.pop();
            s.pop();
            u=s.top();
            s.push(GOTO(u,"T"));
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