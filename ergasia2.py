n=int(input("Enter an integer:"))
print("Factors are:")

i=2
j=1
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
                print("(",tab[i],"**",c,")")
            else:
                print("(",tab[i],")")
except IndexError:
    gotdata = 'null'
            
