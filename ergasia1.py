


def sumIntervals(tab):
    l=[]
    c=0
    flag=False
    sum=0
    for i in range(0,len(tab)):
        sum= sum+(tab[i][1]-tab[i][0])
        for j in range(tab[i][0],tab[i][1]+1):
            if j not in l:
                l.append(j)
            elif j!= tab[i][0] :
                if j==tab[i][1] and flag==True :
                    c=c+1
                c=c+1
            else:
                flag=True
    sum=sum-c             
    
              
    print(sum)       



sumIntervals( [[1,2], [6, 10], [11, 15] ] ) 
sumIntervals( [[1,4], [7, 10], [3, 5] ] ) 
sumIntervals( [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]] )
