list_1=[10,20,30,40,50,60,70,809,0]

def square_num(num):
    
    return num*num


#squaring with the help of map function
squared_list=(map(square_num,list_1))
print(type(squared_list))


#squaring with the help of for loop
list_2=[]
for i in list_1:
    list_2.append(i*i)

print(list_2)