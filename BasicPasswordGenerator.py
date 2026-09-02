import random
choice=int(input("enter passwordlength:"))
choices=["1",'2',"3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","M","O","P","Q","R","S","T","U","U","V","W","X","Y","Z","@","%","&","*","(",")","!"]
passwordlist=[]
for i in range(choice):
    passwordlist.append(random.choice(choices))

password="".join(passwordlist)
print(f"your password of {choice} length is:{password}")
