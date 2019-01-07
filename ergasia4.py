
word=input("write here:")

tab=list(word)
flag=False
print(tab)
s=" "
i=0
c=0

for i in range(0,100):
  
 try:   
  if(tab[i]=="o"and tab[i+1]=="n"and tab[i+2]=="e"):
   if(flag==False):
    a=1
    flag=True
   else:
       b=1
  if(tab[i]=="t"and tab[i+1]=="w"and tab[i+2]=="o"):
   if(flag==False):
    a=2
    flag=True
   else:
       b=2
  if(tab[i]=="s"and tab[i+1]=="i"and tab[i+2]=="x"):
   if(flag==False):
    a=6
    flag=True
   else:
    b=6
 except IndexError:
      gotdata = 'null'
 try: 
   if(tab[i]=="f"and tab[i+1]=="o"and tab[i+2]=="r"and tab[i+3]=="e"):
    if(flag==False):
     a=4
     flag=True
    else:
       b=4
   if(tab[i]=="f"and tab[i+1]=="i"and tab[i+2]=="v"and tab[i+3]=="e"):
    if(flag==False):
     a=5
     flag=True
    else:
       b=5
   if(tab[i]=="n"and tab[i+1]=="i"and tab[i+2]=="n"and tab[i+3]=="e"):
    if(flag==False):
     a=9
     flag=True
    else:
       b=9
   if(tab[i]=="z"and tab[i+1]=="e"and tab[i+2]=="r"and tab[i+3]=="o"):
    if(flag==False):
     a=0
     flag=True
    else:
       b=0
 except IndexError:
      gotdata = 'null'
 try:       
    if(tab[i]=="t"and tab[i+1]=="h"and tab[i+2]=="r"and tab[i+3]=="e"and tab[i+4]=="e"):
     if(flag==False):
      a=3
      flag=True
     else:
      b=3
    if(tab[i]=="s"and tab[i+1]=="e"and tab[i+2]=="v"and tab[i+3]=="e"and tab[i+4]=="n"):
     if(flag==False):
      a=7
      flag=True
     else:
       b=7
    if(tab[i]=="t"and tab[i+1]=="i"and tab[i+2]=="g"and tab[i+3]=="h"and tab[i+4]=="t"):
     if(flag==False):
      a=8
      flag=True
     else:
       b=8
   
 except IndexError:
      gotdata = 'null'

 try:
     if(tab[i]=="p"and tab[i+1]=="l"and tab[i+2]=="u"and tab[i+3]=="s"):
      s="+"
     if(tab[i]=="m"and tab[i+1]=="i"and tab[i+2]=="n"and tab[i+3]=="u"and tab[i+4]=="s"):
      s="-"
     if(tab[i]=="t"and tab[i+1]=="i"and tab[i+2]=="m"and tab[i+3]=="e"and tab[i+4]=="s"):
      s="*"

 except IndexError:
      gotdata = 'null'
    
if(s=="+"):
 c=a+b
if(s=="-"):
 c=a-b
if(s=="*"):
 c=a*b
print("exw",repr(a))
print("exw",repr(b))
print("to prosi einai: ",s)
print("h lysi einai",repr(c))

