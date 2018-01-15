from sys import getsizeof
nc=list()
pi_chart=list()
a=list()
order=0
result=list()
tot_reduc=0
var=list()
def set_var():
    global var
    var.clear()
    i=0
    while i<order:
        var.append(chr(65+i))
        i=i+1  
def printexp(st):
    global var
    i=0
    while i<order:
        if st[i]=='1':
            print(var[i],end='')
        elif st[i]=='0':
            print(var[i]+"'",end='')
        else:
            pass
        i=i+1
    
def dupdel(l):
    for i in range(len(l)):
            j=i+1
            while j<len(l):
                    if l[i][0:order-1]==l[j][0:order-1]:
                            del l[j]
                            j=j-1
                    j=j+1                            
    
def find_nc(l,m):
        if(len(l)==0 or len(m)==0):
                pass
        else:
                for i in range(len(m)):
                        for j in range(len(m[i])):
                                if m[i][j]==False:
                                        nc.append(l[i][j])
                                       
def get_nci(l):
        l1=list()
        if(len(l)==0):
                pass
        else:
                for i in l:
                        temp=[False]*len(i)
                        l1.append(temp)                                  
        return l1                        
                                
def check(s,nou):
        c=0
        for k in range(order):
                  if s[k]=='_':
                      c=c+1
                  elif s[k]=='(':
                          c=100
        if c!=nou:    
                return False
        else:
                return True
        
def my_slice(s):
	for i in range(len(s)):
		if s[i]=='(':
			f=i
		if s[i]==')':
			l=i
	return s[f+1:l]

def take_input():
    pi_chart.clear()
    nc.clear()
    result.clear()
    global tot_reduc
    tot_reduc=0
    global a
    a=input("\u2211-")
    a=a.split(sep=',')
    mx=eval(a[0])
    for i in a:
            if eval(i)>mx:
                    mx=eval(i)
    global order
    order=len(bin(mx)[2:])          
    b=list()
    for i in range(len(a)):
        b.append(dict())   
        num=eval(a[i])
        b[i]['binary']=bin(num)[2:].zfill(order)+"("+a[i]+")"
        s=0
        for j in range(order):
            s=s+eval(b[i]['binary'][j])
        b[i]['sod']=s            
    m=b[0]['sod']
    for i in range(len(a)):
        if m<b[i]['sod']:
            m=b[i]['sod']
    c1=list()
    for i in range(m+1):
        c1.append(list())
    for i in range(len(b)):
        c1[b[i]['sod']].append(b[i]['binary'])
    for i in c1:
            dupdel(i)
    return c1
def combiner(c1,nou=1):
    nc_index=get_nci(c1)   
    s1=str()
    l1=list()
    c2=list()
    for i in range(len(c1)-1):
        if len(c1[i])==0:
            pass
        else:
            l1=[]
            for l in range(len(c1[i])):
                temp=c1[i][l]
                for j in range(len(c1[i+1])) :
                    s1=""
                    for k in range(order):
                        try:                 
                            add=(eval(temp[k])+eval(c1[i+1][j][k]))
                            if add==1:
                                s1=s1+"_"
                            else:
                                s1=s1+temp[k]
                        except:
                             if temp[k]==c1[i+1][j][k]:
                                 s1=s1+temp[k]
                             else:
                                 pass
                    s1=s1+"("+my_slice(temp)+","+my_slice(c1[i+1][j])+")"         
                    ch=check(s1,nou)
                    if ch:
                            l1.append(s1)
                            nc_index[i][l]=True
                            nc_index[i+1][j]=True
                            
            c2.append(l1)
    find_nc(c1,nc_index)
    for i in c2:
            dupdel(i)
    return c2         
def prin():
        print("\nNON-ESSENTIAL PRIME IMPLICANTS-")
        for i in range(len(nc)-1):
                print(nc[i]+",",end='')        
        print(nc[-1],end=' ')
        print("\nOR")
        for i in range(len(nc)-1):
            printexp(nc[i])
            print(" , ",end='')
        printexp(nc[-1])      
        print("\nANY COMBINATION OF ABOVE IMPLICANTS WITH ESSENTIAL PIs(IF ANY) CONTAINING ALL INPUTS IS VALID")
def search(val):
        global a
        for i in range(len(a)):
                if val==a[i]:
                        return i
        
def generatepic():
        global a
        global pi_chart
        for i in range(len(nc)):
                sub=[' ']*len(a)
                ar=my_slice(nc[i]).split(sep=',')
                for j in range(len(ar)):
                        pos=search(ar[j])
                        sub[pos]='X'
                pi_chart.append(sub)
def print_chart(l):
        x=' '
        if len(nc):      
                print("PI"+x*(len(max(nc,key=len))-len("PI")),end=' ')
                for each in a:
                        print(each,end=" ")
                print("\n")
                for i in range(len(nc)):
                        print(nc[i]+x*(len(max(nc,key=len))-len(nc[i])),end=" ")
                        for j in range(len(a)):
                                try:   
                                        if eval(a[j+1])>9 and eval(a[j+1])<99:
                                                print(l[i][j],end="  ")
                                        elif eval(a[j+1])>99:
                                                print(l[i][j],end="    ")
                                        else:
                                                print(l[i][j],end=" ")
                                except:
                                        print(l[i][j],end=" ")
                        print("\n")                
                                         
        else:
                print("PI CHART EMPTY")
def get_pic():
        return pi_chart
def empty(seq):
        c=0
        for i in seq:
                if len(i)!=0:
                        c=1
        return c                
                
def reduce(pi):
        global a
        global result
        global tot_reduc
        rtod=list()
        posx=list()
        if(len(pi)==0):
                tot_reduc=1
        elif not empty(pi):
                nc.clear()
                tot_reduc=1
        else:
                
                j=0
                while(j<len(pi[0])):
                        c=0
                        i=0
                        while(i<len(pi)):
                                if pi[i][j]=='X':
                                        c=c+1
                                        if c==1:
                                                r=i
                                i=i+1        
                        if c==1:
                                rtod.append(r)
                                k=0
                                while(k<len(pi)):
                                        del pi[k][j]
                                        k=k+1
                                del a[j]
                                j=j-1
                        j=j+1
                rtod=list(set(rtod))
                rtod.sort()
                i=0
                while i<len(rtod):
                        j=0
                        while j<len(pi[rtod[i]]):
                                if pi[rtod[i]][j]=='X':
                                        k=0
                                        while k<len(pi):
                                                del pi[k][j]
                                                k=k+1
                                        del a[j]
                                        j=j-1
                                j=j+1        
                        i=i+1
                i=0
                while(i<len(rtod)):
                        try:
                                del pi[rtod[i]]
                                result.append(nc[rtod[i]])
                                del nc[rtod[i]]
                                for j in range(len(rtod)):
                                        rtod[j]=rtod[j]-1
                                i=i+1
                        except:
                                i=i+1
                                
                                
def get_result():
    set_var()
    print("ESSENTIAL PRIME IMPLICANTS-")
    if len(result):
        for i in range(len(result)-1):
                print(result[i]+"+",end='')        
        print(result[-1],end=' ')
        print("\nOR")
        for i in range(len(result)-1):
            printexp(result[i])
            print(" + ",end='')
        printexp(result[-1])
def get_totreduc():
        return tot_reduc
def x_count(l):
        c=0
        for i in l:
                if i=='X':
                        c=c+1
        return c 
    
def r_dom(pi):
    xpos=list()
    sxpos=list()
    i=0
    while i<len(pi):
        sxpos=[]
        j=0
        while j<len(pi[i]):
            if pi[i][j]=='X':
                sxpos.append(j)
            j=j+1    
        xpos.append(sxpos)
        i=i+1   
    i=0
    while i<len(pi):
        j=i+1
        while j<len(pi):
            if len(set(xpos[i]+xpos[j]))==len(xpos[j]):
                del pi[i]
                del nc[i]
                del xpos[i]
                i=i-1
                break
            elif len(set(xpos[i]+xpos[j]))==len(xpos[i]):
                del pi[j]
                del nc[j]
                del xpos[j]
                j=j-1
            else:
                pass
            j=j+1
        i=i+1
        
def c_dom(pi):
    xcc=list()
    xnc=list()
    sxnc=list()
    j=0
    if len(pi):
        while j<len(pi[0]):
            xcc=[]
            i=0
            while i<len(pi):
                if pi[i][j]=='X':
                    xcc.append(i)
                i=i+1    
            k=j+1
            xnc.clear()
            while k<len(pi[0]):
                l=0
                sxnc=[]
                while l<len(pi):
                    if pi[l][k]=='X':
                        sxnc.append(l)
                    l=l+1
                xnc.append(sxnc)
                k=k+1
            i=0
            while i<len(xnc):
                if len(set(xcc+xnc[i]))==len(xcc):
                    r=0
                    while r<len(pi):
                        del pi[r][j]
                        r=r+1
                    del a[j]    
                    i=len(xnc)
                    j=j-1
                elif len(set(xcc+xnc[i]))==len(xnc[i]):
                    r=0
                    while r<len(pi):
                        del pi[r][j+i+1]
                        r=r+1
                    del a[j+i+1]    
                    i=len(xnc)
                    j=j-1
                else:
                    pass
                i=i+1        
            j=j+1
    else:
        global tot_reduc
        tot_reduc=1
        return
             
def get_order():
        return order
def get_size(l):
    size=0
    for i in l:
        size=size+getsizeof(i)
    return size    

    
        
        


                        
                               
                
                       
                        
                
                
        
                
                

        
        

        




                                
                                
