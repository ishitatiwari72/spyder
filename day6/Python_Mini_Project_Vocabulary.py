

"""
Code Challenge
  Name: 
    Vocabulary
  Filename: 
    Vocabulary.py
  Problem Statement:
    Novel = james_joyce_ulysses.txt
    The claim is that James Joyce used in his novel more words than any other author. 
    Actually his vocabulary is above and beyond all other authors, 
    maybe even Shakespeare.
    
    1. Find the total number of words in the novel
    2. many words occur multiple time:["the", "while", "good", "bad", "ireland", "irish"]
    3. Quality of a novel is the number of different words.
       Find the number of different words used
    4. look at the other novels and find the total words and unique words for comparison
       novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt']

    5. Special Words in Ulysses novel by comparing with others, 
       words which are only used in Ulysses, store it in a file

    6. Common Words - Find the words which occur in every book.

  Hint: 
     Use Sets, Regex, File Handling
     re.findall(r"\b[\w-]+\b", ulysses_txt)
     

"""
dic={}
list1=[]
#list2=[]
word=0
set1=set()
f1= open('james_joyce.txt',errors='ignore')
for item in f1:
    list1.append(item.split())
for item1 in list1:
    word=word+len(item1)
print("total words >>",word)



for item in list1:
    for item1 in range(0,len(item)):
      
            dic[item[item1]]=int(dic.get([item[item1]],0))+1

                                                                                                                                                
            

set1=set(list1)
for item in list1:
    
    word=word+int(item.split(" "))
    list1.append(item.split(" "))