# 2 problem : to determin the longest length subsequence
#string 1= x string 2=y
import string,random
def func(x,y):
    table=[[0 for i in range(len(x)+1)]for j in range( len(y)+1)]
    for i in  range(0 ,len(y)):
        for j in range(0,len(x)):
            if(y[i]==x[j]):
                c=table[i][j]+1
            else:
                c=max(table[i][j+1],table[i+1][j])
            table[i+1][j+1]=c            
    print_table(table)
    
    #x=string_determination(table,x)
    x=print_all_list(table,x)
    return x
def string_determination(table,x):
    N=len(table)-1
    M=len(table[N])-1
    #print N,M
    i=N
    j=M
    d=[]
    flag=[]
    q=0
    while(i>0 and j>0):
        if(table[i][j]==max(table[i-1][j],table[i-1][j-1],table[i][j-1])):           
           if(table[i][j]==table[i-1][j]):
               i=i-1
           else:
               j=j-1           
        else:           
           i=i-1
           j=j-1
           d.append(x[j])#d+=x[j]    
    d.reverse()
    print flag
    return d
def print_all_list(table,x):
    N=len(table)-1
    M=len(table[N])-1
    #print N,M
    i=N
    j=M
    d=[]
    flag=[]
    q=0
    while(i>0 and j>0):
        if(table[i][j]==max(table[i-1][j],table[i-1][j-1],table[i][j-1])):           
           if(table[i][j-1]==table[i-1][j]):
               flag.append(i)
               flag.append(j)
               i=i-1
           else:
                if(table[i][j]==table[i-1][j]):
                   i=i-1
                else:
                    j=j-1
        else:           
           i=i-1
           j=j-1
           d.append(x[j])
                
    print flag
    d.reverse()
    return d
        
def print_table(t):
    for i in range(len(t)):
        print t[i]

if(__name__=='__main__'):
    x='BDCABA'#random.sample(range(0,13),7)#'BDCABA'
    y='ABCBDAB'#random.sample(range(0,9),8)#'ABCBDAB'
    print x,y
    print func(x,y)

    
