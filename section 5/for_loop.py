list1=[1,2,3,4,5,6,7,8,9,10]


#check even number
for  i in list1:
    if(i%2==0):
        print('this is even number {}'.format(i))
    else:
        print('this is odd number {}'.format(i))
        
        
sumOfList=0

for i in [10,20,30,40,50]:
    sumOfList=sumOfList+i
    
print('sum of list :{}'.format(sumOfList))


name='MyNameIsKajiwala'

for i in name:
    print(i)
    
    
    
tuple1=[(1,3,2),(3,4,4),(5,4,6)]
#tuple unpacking
for a,b,c in tuple1:
    print(b)
    
    
dict1={'k1':'value1','k2':'value2','k3':'value3'}


for key,value in dict1.items():
    print("{k} --> {v}".format(k=key,v=value))
    