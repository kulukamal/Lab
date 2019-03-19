#include<bits/stdc++.h>

void f1(char, int, int); 
void f2(char, int, int); 
void f3(char c); 

int count, n = 0; 

char First[10][100]; 

char Follow[10][100]; 
int m = 0; 

char input[10][10]; 
char f[10], first[10]; 
int k; 
char ck; 
int e; 

int main(int argc, char **argv) 
{ 
    int jm = 0; 
    int km = 0; 
    int flag=1;
    int flagCount=0;
    std::set<std::pair<char,char> > nt; 
    std::set<int> pt;
    int i, choice; 
    char c, ch; 
    scanf("%d",&count);
    for(int i=0;i<count;i++){
        scanf("%s",input[i]);
        if(input[i][0]==input[i][2])flag=0;
        nt.insert(std::make_pair(input[i][0],input[i][2]));
    }
    if(nt.size()!=count)flag=0;
    if(!flag)
    {
        printf("Invalid LL(1) Grammar.\n");
        exit(0);
    }
    int ptr1; 
    char visited[count]; 
    int ptr = -1; 
    
    for(k = 0; k < count; k++) { 
        for(ptr1 = 0; ptr1 < 100; ptr1++) { 
            First[k][ptr1] = '!'; 
        } 
    } 
    int p1 = 0, p2, xxx; 
    
    for(k = 0; k < count; k++) 
    { 
        c = input[k][0]; 
        p2 = 0; 
        xxx = 0; 
        
        for(ptr1 = 0; ptr1 <= ptr; ptr1++) 
            if(c == visited[ptr1]) 
                xxx = 1; 
                
        if (xxx == 1) 
            continue; 
        
        f2(c, 0, 0); 
        ptr += 1; 
        
        visited[ptr] = c; 
        printf("\n First(%c) =  ", c); 
        First[p1][p2++] = c; 
        
        for(i = 0 + jm; i < n; i++) { 
            int ptr2 = 0, chk = 0; 
            
            for(ptr2 = 0; ptr2 < p2; ptr2++) { 
                
                if (first[i] == First[p1][ptr2]) 
                { 
                    chk = 1; 
                    break; 
                } 
            } 
            if(chk == 0) 
            { 
                if(first[i]=='^')pt.insert(p1);
                printf("%c ", first[i]); 
                First[p1][p2++] = first[i]; 
            } 
        } 
        printf("\n"); 
        jm = n; 
        p1++; 
    } 
    printf("\n"); 
    char visitede[count]; 
    ptr = -1; 
    
    for(k = 0; k < count; k++) { 
        for(ptr1 = 0; ptr1 < 100; ptr1++) { 
            Follow[k][ptr1] = '!'; 
        } 
    } 
    p1 = 0; 
    for(e = 0; e < count; e++) 
    { 
        ck = input[e][0]; 
        p2 = 0; 
        xxx = 0; 
        
        for(ptr1 = 0; ptr1 <= ptr; ptr1++) 
            if(ck == visitede[ptr1]) 
                xxx = 1; 
                
        if (xxx == 1) 
            continue; 
        
        f3(ck); 
        ptr += 1; 
        
        visitede[ptr] = ck; 
        printf(" Follow(%c) =  ", ck); 
        Follow[p1][p2++] = ck; 
        for(i = 0 + km; i < m; i++) { 
            int ptr2 = 0, chk = 0; 
            for(ptr2 = 0; ptr2 < p2; ptr2++) 
            { 
                if (f[i] == Follow[p1][ptr2]) 
                { 
                    chk = 1; 
                    break; 
                } 
            } 
            if(chk == 0) 
            { 
                if(pt.find(p1)!=pt.end())
                {
                    char ch = f[i];
                    for(int l=1;First[p1][l]!='!';++l)
                    {
                        if(ch==First[p1][l])flag=0;
                    }
                }
                printf("%c ", f[i]); 
                Follow[p1][p2++] = f[i]; 
            } 
        } 
        printf(" \n\n"); 
        km = m; 
        p1++; 
    } 

    if(flag)
        printf("Valid LL(1) Grammar.\n");
    else
        printf("Invalid LL(1) Grammar.\n");
} 

void f3(char c) 
{ 
    int i, j; 
    
    if(input[0][0] == c) { 
        f[m++] = '$'; 
    } 
    for(i = 0; i < 10; i++) 
    { 
        for(j = 2;j < 10; j++) 
        { 
            if(input[i][j] == c) 
            { 
                if(input[i][j+1] != '\0') 
                { 
                    f1(input[i][j+1], i, (j+2)); 
                } 
                
                if(input[i][j+1]=='\0' && c!=input[i][0]) 
                { 
                    f3(input[i][0]); 
                } 
            } 
        } 
    } 
} 

void f2(char c, int q1, int q2) 
{ 
    int j; 
    
    if(!(isupper(c))) { 
        first[n++] = c; 
    } 
    for(j = 0; j < count; j++) 
    { 
        if(input[j][0] == c) 
        { 
            if(input[j][2] == '^') 
            { 
                if(input[q1][q2] == '\0') 
                    first[n++] = '^'; 
                else if(input[q1][q2] != '\0'
                        && (q1 != 0 || q2 != 0)) 
                { 
                    f2(input[q1][q2], q1, (q2+1)); 
                } 
                else
                    first[n++] = '^'; 
            } 
            else if(!isupper(input[j][2])) 
            { 
                first[n++] = input[j][2]; 
            } 
            else
            { 
                f2(input[j][2], j, 3); 
            } 
        } 
    } 
} 

void f1(char c, int c1, int c2) 
{ 
    int k; 
    
    if(!(isupper(c))) 
        f[m++] = c; 
    else
    { 
        int i = 0, j = 1; 
        for(i = 0; i < count; i++) 
        { 
            if(First[i][0] == c) 
                break; 
        } 
        
        while(First[i][j] != '!') 
        { 
            if(First[i][j] != '^') 
            { 
                f[m++] = First[i][j]; 
            } 
            else
            { 
                if(input[c1][c2] == '\0') 
                { 
                    f3(input[c1][0]); 
                } 
                else
                { 
                    f1(input[c1][c2], c1, c2+1); 
                } 
            } 
            j++; 
        } 
    } 
} 
