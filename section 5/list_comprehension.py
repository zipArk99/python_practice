name='shaurya'

#with list comprehension 
myList=[letter for letter in name if letter in ['a','e','i','o','u']]
print("myList::{}".format(myList))

#without list Comprehension
myList2=[]
for letter in name:
    if(letter in ['a','e','i','o','u']):
        myList2.append(letter)
print("myList2::{}".format(myList2))