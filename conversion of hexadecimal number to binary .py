def dec(x):
  k=[]
  n=x
  while(n>0):
    a=int(float(n%2))
    k.append(a)
    n=(n-a)/2
  k.append(0)
  string=" "
  for j in k[::-1]:
    string=string+str(j)
  if(len(string)>4):
    print(string[1:],end=" ")
  elif
