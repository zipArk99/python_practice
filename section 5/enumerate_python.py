

x=[10,20,30,40,50,[100,200,300]]
    

#if want to get iteration count without enumerate
counter=0
for i in x:
    print("{c}-->{v}".format(c=counter,v=i))
    counter+=1
    
#with enumerate
for index,value in enumerate(x):
    print('{i}--->{v}'.format(i=index,v=value))
    if(type(value)==list):
        for value2 in value:
            print(value2)
            
            
for i in enumerate(x):
    print(type(i))
