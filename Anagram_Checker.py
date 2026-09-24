def anagram_checker(word1,word2):
  arrange1=list(word1)
  arrange2=list(word2)
  arrange1.sort()
  arrange2.sort()
  sorted1="".join(arrange1)
  sorted2="".join(arrange2)
  if(sorted1==sorted2):
    print(f"anagram")
  else:
    print(f"not anagram")

print("======Anagram Checker=====")
word1=input("enter word:").lower()
word2=input("enter word:").lower()
anagram_checker(word1,word2)
  