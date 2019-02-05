#include<stdio.h>
#include<string.h>
#include<iostream.h>
void main()
{
char in[10],ch[10],p[10],pb[10][10];
int i,j,n,f;
cout<<"\nEnter tne no of productions";
cin>>n;
cout<<"\nEnter the production and production body";
for(i=0;i<n;i++)
{
cout<<"\nproduction";
cin>>p[i];
cout<<"\nproduction body";
cout<<p[i]<<"->";
cin>>pb[i];
cout<<"\n";
}
for(i=0;i<n;i++)
{
for(j=0;j<3;j++)
{
if(p[i]==pb[0][j])
{
pb[0][j]=pb[i][0];
cout<<pb[0];
cout<<"\n";
}
}
}
cout<<"\nEnter the input string";
cin>>in;
i=0;
for(j=0;j<n;j++)
{
if(pb[0][j]==in[i])
{
f++;
i++;
}
}
if(f==3)
{
cout<<"\naccepted";
}
else
{
cout<<"\n not accepted";
}
getch();
}