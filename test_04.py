import random

list = ["a","b","c","d","A","e","B","f"]
# for index,item in enumerate(list):
   # print(index+1,item)
   #  if index % 2 == 0:
   #      print(item+"\t\t",end="")
   #  else:
   #      print(item+"\n")
print(list.count("a"))
list.sort(key=str.lower)
print(list)

list2 = [random.randint(20,40) for i in range(34)]
print( list2)
