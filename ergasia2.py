n=int(input("Enter an integer:"))
print("Factors are:")

i=2
j=1
final=[]
apotel=[]
tab=[]
flag=True
while n>1: 
    while n%i==0:
                     
        if (n%i==0 and flag==True):
            
             if(i!=1):
                
                tab.append(i)
                
             n=n/i
               
    i=i+1    

try:
    for i in range(0,len(tab)):
        c=0
        for j in range(0,len(tab)):
            
            if (tab[i]==tab[j] and tab[i-1]!=tab[i]):
                c=c+1                       
        if tab[i] not in apotel:                  
            apotel.append(tab[i])
            if(c>1):
                a="("+repr(tab[i])+"**"+repr(c)+")"
                final.append(a)
            else:
                a="("+repr(tab[i])+")"
                final.append(a)
except IndexError:
    gotdata = 'null'
            
print(''.join(final))
