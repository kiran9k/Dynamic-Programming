a=[[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]

b=[[0 for i in range(len(a))]for j in range (len(a))]
key=[[0 for i in range(len(a))]for j in range (len(a))]

def print_array(a):
    for i in range(len(a)):
        print a[i]

def func(a):
    N=len(a)
    x=1
    for i in range(0,N-1):
        for j in range(0,N-i-1):
                cost(a,j,x+j)
        x=x+1    
def cost(a,i,j):
    x=0
    temp=[]
    temp1=[]
    for k in range(i,j):
        x+=b[i][k]
        x+=b[k+1][j]
        x+=a[i][0]*a[k][1]*a[j][1]
        temp.append(x)
        temp1.append(k)
        x=0    
    b[i][j]=min(temp)
    x=temp.index(b[i][j])
    key[i][j]=temp1[x]
            

        
        
   
def print_paranthesis(key,p,q):
    if(p==q):
        #print '(',
        print 'A%d'%(p),
        
    else:
        print'(',
        print_paranthesis(key,p,key[p][q])
        print '*',
        
        print_paranthesis(key,key[p][q]+1,q)
        print ')',
    
    
        
if (__name__=='__main__'):
    func(a)## calculates the table
    print_array(b)
    print "#### Key ####"
    print_array(key)
    temp=[]
    print_paranthesis(key,0,len(a)-1)




























