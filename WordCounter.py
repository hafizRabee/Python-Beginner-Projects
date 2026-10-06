def WordCounter(sentence):
  L=sentence.split() # withot " " split automatically handle multiple spaces
  
  return len(L)
sentence=input("enter sentence:")
print(f"total words count:{WordCounter(sentence)}")