#checker board
#problem to find the path for the maximum sum of all available paths
#condition : len of 2D matrix must be equal to len of  any one row of its elemtns
import random
def func(a):    
    N=len(a)
    if(N==0):
        return '[]'
    else:
        try:
            M=max(len(a[i]) for i in range(0,len(a)))
            if(M<=N):
                M=N            
            sum_table=[[0 for i in range(0,N+2)]for j in range(0,N+1)]
            key_table=[[0 for i in range(0,N+1)]for j in range(0,N+1)]
            for i in range(0,N):
                #if the matrix is not a perfect square: 
                #append 0's at end to make it a perfect square
                if(len(a[i])<M):
                    for k in range(N,M):
                        a[i].append(0)
                #appending ends
                for j in range(0,N):
                    cost(a,i,j,sum_table,key_table)
            solution=traversal(key_table,sum_table,a)
            return solution
        except:
            return(max(a))       
    
def cost(a,i,j,sum_table,key_table):
    x=max(sum_table[i][j],sum_table[i][j+1],sum_table[i][j+2])
    y=sum_table[i].index(x,j,j+3)    
    sum_table[i+1][j+1]=x+a[i][j]
    key_table[i+1][j+1]=y
def traversal(key_table,sum_table,a):
    d=[]
    N=len(sum_table)-1
    x=max(sum_table[N])
    y=sum_table[N].index(x)    
    d.append(a[N-1][y-1])    
    for i in range(N-1,0,-1):
        y=key_table[i+1][y]    
        d.append(a[i-1][y-1])
    return d
    

def print_func(a):
    for i in range(0,len(a)):
        print a[i]
if(__name__=='__main__'):
    #a=[[1,2]]
    a=[]
    for i in range(0,5):
        a.append([])
        a[i]=random.sample(range(-5,10),5)
    #a=[]
    #a=[[2,3],[3,-9]]
    #a=[[2,3,-9,5],[1,2,34,5],[4,5,2,-4],[2,-3,4,5]]
    #a=[[0.2,0.1,0,0.7,0.3],[1.5,1.2,1.0,1.1,1.0],[2.1,2.5,3.0,2.0,2.8],[3.1,3.7,3.9,4.0,3.1], [5.1,4.8,2.3,4.0,5.3]]
    print_func(a)
    print ""    
    x= func(a)    
    print "solution is"
    print x
    
