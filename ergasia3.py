filename=input("dose onoma arxeiou: ")+".py"
opfile  = open(filename, "r")
lines = opfile.readlines()
opfile.close()  
opfile= open(filename,"w")
try:
    for line in lines:
       print(line)
       tab=list(line)
       
       for i in range(0,len(tab)):
           if tab[i]=="#":
              for j in range(i,len(tab)):
                    tab[j]=""
                    
       print("comments deleted:")             
       line=''.join(tab)
       print(line,"\n")
       opfile.write(line)
       opfile.write("\n")
except IndexError:
    gotdata = 'null'

opfile.close()
    
              






    
