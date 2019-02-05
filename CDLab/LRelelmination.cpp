#include<bits/stdc++.h>
using namespace std;
main()
{
	vector<string> grammer;
	string tmp;
	int n;
	map<char,vector<string> > rules;
	cout<<"No of rules :";
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		cin>>tmp;
		grammer.push_back(tmp);
		string str = tmp.substr(3,tmp.length()-3);
		int count = 0,pos=0;
		for(int j=0;j<str.length();++j)
		{
			if(str[j]=='|')
			{
				rules[tmp[0]].push_back(str.substr(pos,count));
				pos=j+1;
				count=0;
			}
			else
			{
				count++;
			}
		}
		rules[tmp[0]].push_back(str.substr(pos,count));
	}
		map<char,vector<string> > ::iterator it;
		map<string,vector<string> > newRules;
		for(it = rules.begin();it!=rules.end();it++)
		{
			char s = it->first;
			ostringstream stringStream;
			stringStream <<s<<"'";
			string S = stringStream.str();
			vector<string> v,u,w;
			string str;
			int flag=0;
			u = it->second;
			for(int i =0;i<u.size();++i)
				{
					if(u[i][0]==s)
					{
						string t = u[i].substr(1,u[i].length()-1)+S;
						v.push_back(t);
						flag=1;
					}
					else
					{
						
					}
				}
			if(flag)
			{
				for(int i =0;i<u.size();++i)
				{
					if(u[i][0]==s)
					{
					
					}
					else
					{
						w.push_back(u[i]+S);
					}
				}
			}
			else
			{
				for(int i =0;i<u.size();++i)
				{
					if(u[i][0]==s)
					{
					
					}
					else
					{
						w.push_back(u[i]);
					}
				}
			}
			cout<<endl;
			it->second = w;
			v.push_back("^");
			if(flag)
			newRules[S]=v;
		}
		cout<<"---------------\n\n";
		for(it = rules.begin();it!=rules.end();it++)
		{
			cout<<it->first<<" -> ";
			for(int i =0;i<it->second.size();++i)
				{
					if(i!=it->second.size()-1)
					cout<<it->second[i]<<" | ";
					else
					cout<<it->second[i];
				}
			cout<<endl;
		}
		map<string,vector<string> > ::iterator it1;
		for(it1 = newRules.begin();it1!=newRules.end();it1++)
		{
			cout<<it1->first<<" -> ";
			for(int i =0;i<it1->second.size();++i)
				{
					if(i!=it1->second.size()-1)
					cout<<it1->second[i]<<" | ";
					else
					cout<<it1->second[i];
				}
			cout<<endl;
		}

}