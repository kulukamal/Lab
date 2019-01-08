#include<bits/stdc++.h>
using namespace std;

main()
{
	char str[80];
	int flag=1,noOfZero=0,noOfOne=0;
	scanf("%[^\n]",str);
	for(int i=0;i<strlen(str);++i)
	{
		if(str[i]-'0' == 0)noOfZero++;
		if(str[i]-'0' == 1)noOfOne++;
	}
	if(noOfOne%2==1 || noOfZero%2==0)
		flag=0;
	if(flag)
		cout<<"accepted"<<endl;
	else
		cout<<"not-accepted"<<endl;
}