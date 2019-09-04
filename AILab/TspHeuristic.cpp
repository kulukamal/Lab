#include<bits/stdc++.h>
#define lli long long int
#define INF 10000000
#define N 5

using namespace std;

int main()
{
	lli C[N][N]= {{INF,1,6,8,4},{7,INF,8,5,6},{6,8,INF,9,7},{8,5,9,INF,8},{4,6,7,8,INF}};
	lli perm[4] = {1,2,3,4};
	lli i,j,k;
	lli ans = INF;
	do
	{
		lli curr = C[0][perm[0]];
		for(i=1;i<4;i++)
		{
			curr += C[perm[i-1]][perm[i]];
		}
		curr += C[perm[3]][0];
		ans = min(ans,curr);
	}
	while(next_permutation(perm,perm+4));
	
	cout<<ans<<endl;
}

