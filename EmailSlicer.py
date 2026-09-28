def emailslicer(n):
  if("@" not in n):
    print("invalid email")
  elif(n.startswith(".") or n.endswith(".")):
    print("please enter Valid email")
  elif(" " in n):
    print("please enter valid email")
  
  elif(n.count("@")!=1):
     print("please enter valid email")
  else:
   index=n.find("@")
   username=n[:index]
   domain=n[index+1:]
   if(username=="" or domain==""):
     print("please enter email with username and domain name")
   elif("." not in domain):
    print("please enter valid email")
   else:
     print("username:",username,sep="")
     print("domain:",domain,sep="")
n=input("enter email:")
emailslicer(n)