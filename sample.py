
filename=input("dose onoma arxeiou: ")+".py"#comment to be deleted
opfile  = open(filename, "r")#comment to be deleted
lines = opfile.readlines()#comment to be deleted
opfile.close()  
opfile= open(filename,"w")#comment to be deleted
try:
    for line in lines:
       print(line)
       tab=list(line)#comment to be deleted
       
       for i in range(0,len(tab)):
           if tab[i]=="#":
              for j in range(i,len(tab)):#comment to be deleted
                    tab[j]=""
                    
       print("comments deleted:")   #comment to be deleted          
       line=''.join(tab)
       print(line,"\n")
       opfile.write(line)#comment to be deleted
       opfile.write("\n")
except IndexError:#comment to be deleted
    gotdata = 'null'

opfile.close()


