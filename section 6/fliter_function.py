list_one=[1,2,3,4,5,6,7,8,9,10]


def check_even(num):
    if(num%2==0):
        return num
    
    
even_list=filter(check_even,list_one)
print(even_list)