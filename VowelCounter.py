def counter(sentence):
    count=0
    for i in sentence:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            count+=1
    print(f"total vowels count:{count}")
sentence=input("enter sentence:").lower()
counter(sentence)
   