#include<bits/stdc++.h>
#define lli long long int
#define INF 10000000
#define N 5

using namespace std;

class Node
{
	public:
		lli pos;
		lli cost;
		lli reducedMatrix[N][N];
		lli lowerBound = 0;
		lli level;
		bool vis[N];
		vector<lli> path;
		Node()
		{
			
		}
		
		Node(lli p,lli m[N][N],int l,bool v[N],vector<lli> pa)
		{
			pos = p;
			lli i,j;
			for(i=0;i<N;i++)
			{
				for(j=0;j<N;j++)
					reducedMatrix[i][j] = m[i][j];
			}
			level = l;
			
			for(i=0;i<N;i++)
				vis[i] = v[i];
			vis[pos] = 1;
			
			for(i=0;i<pa.size();i++)
				path.push_back(pa[i]);
			
			path.push_back(pos);
		}
		
		bool reduceRows()
		{
			lli rows[N];
			int i,j;
			for(i=0;i<N;i++)
			{
				rows[i] = INF;
			}
			
			for(i=0;i<N;i++)
			{
				for(j=0;j<N;j++)
				{
					rows[i] = min(rows[i],reducedMatrix[i][j]);
				}
			}
			
			for(i=0;i<N;i++)
			{
				for(j=0;j<N;j++)
				{
					if(rows[i]!=INF && reducedMatrix[i][j]!=INF)
					{
						reducedMatrix[i][j] -= rows[i];
					}
				}
			}
			
			for(i=0;i<N;i++)
			{
				if(rows[i]!=INF)
					lowerBound += rows[i];
			}
		}
		
		bool reduceCols()
		{
			lli cols[N];
			int i,j;
			for(i=0;i<N;i++)
			{
				cols[i] = INF;
			}
			
			for(j=0;j<N;j++)
			{
				for(i=0;i<N;i++)
				{
					cols[j] = min(cols[j],reducedMatrix[i][j]);
				}
			}
			
			for(i=0;i<N;i++)
			{
				for(j=0;j<N;j++)
				{
					if(cols[j]!=INF && reducedMatrix[i][j]!=INF)
					{
						reducedMatrix[i][j] -= cols[j];
					}
				}
			}
			
			for(i=0;i<N;i++)
			{
				if(cols[i]!=INF)
					lowerBound += cols[i];
			}
		}
};

 
bool operator<(const Node& n1, const Node& n2) 
{  
    return n1.cost > n2.cost; 
}

void show(Node n)
{
	cout<<"pos:"<<n.pos<<endl;
	cout<<"cost:"<<n.cost<<endl;
	cout<<"path:"<<endl;
	lli i,j;
	for(i=0;i<n.path.size();i++)
	{
		cout<<n.path[i]<<"->";
	}
	cout<<endl;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(n.reducedMatrix[i][j]!=INF)
			{
				cout<<n.reducedMatrix[i][j]<<" ";
			}
			else
			{
				cout<<"I ";
			}
		}
		cout<<endl;
	}
		
}

int main()
{
	lli C[N][N]= {{INF,1,6,8,4},{7,INF,8,5,6},{6,8,INF,9,7},{8,5,9,INF,8},{4,6,7,8,INF}};
	priority_queue<Node> pq;
	lli i,j,k,ans = -1;
	
	bool v[N];
	memset(v,0,sizeof v);
	
	vector<lli> p;
	
	Node root(0,C,0,v,p);
	root.reduceRows();
	root.reduceCols();
	root.cost = root.lowerBound;
	
	pq.push(root);
	
	while(!pq.empty())
	{
		Node curr = pq.top();
		pq.pop();
		if(curr.level == N-1)
		{
			curr.path.push_back(0);
			cout<<"Answer:"<<endl;
			ans = curr.cost;
			show(curr);
			break;
		}
		
		show(curr);
		
		for(i=0;i<N;i++)
		{
			if(curr.vis[i])
			{
				continue;
			}
			Node n(i,curr.reducedMatrix,curr.level+1,curr.vis,curr.path);
			for(j=0;j<N;j++)
			{
				n.reducedMatrix[curr.pos][j] = INF;
				n.reducedMatrix[j][i] = INF;
			}
			n.reducedMatrix[i][curr.pos] = INF;
			n.reduceRows();
			n.reduceCols();
			n.cost = curr.cost + curr.reducedMatrix[curr.pos][i] + n.lowerBound;
			pq.push(n);
		}
		
	}
}

