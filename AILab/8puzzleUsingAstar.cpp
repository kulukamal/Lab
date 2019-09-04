#include<bits/stdc++.h>
#define lli long long int
#define INF 10000000
#define N 3

using namespace std;
lli start[N][N] = {{0,1,3},{4,2,5},{7,8,6}},goal[N][N] = {{1,2,3},{4,5,6},{7,8,0}};

void print(lli g[N][N])
{
	for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				cout<<g[i][j]<<" ";
			}
			cout<<endl;
		}
}
class Node {
	public :
		lli grid[N][N],h,moves;
		Node *parent;
		
		Node(lli g[N][N],Node *par)
		{
			h = moves = 0;
			for(int i=0;i<N;++i)
				for(int j=0;j<N;++j)
					grid[i][j] = g[i][j];
			print(grid);
			parent = par;
			if(par)
			{
				moves = parent->moves + 1;
			}
			for(int i=0;i<N;i++)
			{
				for(int j=0;j<N;j++)
				{
					for(int l=0;l<N;l++)
					{
						for(int m=0;m<N;m++)
						{
							if(grid[i][j] == goal[l][m])
							{
								h += abs(i-l) + abs(j - m);
							}
						}
					}
				}
			}
			
			cout<<"h = "<<h<<" moves = "<<moves;
			
//			for(int i=0;i<N;i++)
//			{
//				for(int j=0;j<N;++j)
//				{
//					if(grid[i][j] != goal[i][j])
//						h += 1;
//				}
//			}
			h += moves;
			cout<<" f = "<<h<<endl<<endl;
			
			
			
		}
		
};

bool operator<(const Node& n1, const Node& n2) 
{  
    return n1.h > n2.h; 
}

main()
{
	priority_queue<Node> pq;
	Node root(start,NULL);
	
	pq.push(root);
	while(!pq.empty())
	{
		Node u = pq.top();
		pq.pop();
		lli flag = 1;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(u.grid[i][j] != goal[i][j])
				{
					flag = 0;
				}
			}
		}
		if(flag)
		{
			print(u.grid);
			exit(0);
		}
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(u.grid[i][j] == 0)
				{
					if(i-1 > 0)
					{
						lli tmp = u.grid[i][j];
						u.grid[i][j] = u.grid[i-1][j];
						u.grid[i-1][j] = tmp;
						
						Node child(u.grid,&u);
						pq.push(child);
						
						tmp = u.grid[i][j];
						u.grid[i][j] = u.grid[i-1][j];
						u.grid[i-1][j] = tmp;
					}
					if(i+1 > 0)
					{
						lli tmp = u.grid[i][j];
						u.grid[i][j] = u.grid[i+1][j];
						u.grid[i+1][j] = tmp;
						
						Node child(u.grid,&u);
						pq.push(child);
						
						tmp = u.grid[i][j];
						u.grid[i][j] = u.grid[i+1][j];
						u.grid[i+1][j] = tmp;
					}
					if(j-1 > 0)
					{
						lli tmp = u.grid[i][j];
						u.grid[i][j] = u.grid[i][j-1];
						u.grid[i][j-1] = tmp;
						
						Node child(u.grid,&u);
						pq.push(child);
						
						tmp = u.grid[i][j];
						u.grid[i][j] = u.grid[i][j-1];
						u.grid[i][j-1] = tmp;
					}
					if(j+1 > 0)
					{
						lli tmp = u.grid[i][j];
						u.grid[i][j] = u.grid[i][j+1];
						u.grid[i][j+1] = tmp;
						
						Node child(u.grid,&u);
						pq.push(child);
						
						tmp = u.grid[i][j];
						u.grid[i][j] = u.grid[i][j+1];
						u.grid[i][j+1] = tmp;
					}
				}
			}
		}
	}
}














