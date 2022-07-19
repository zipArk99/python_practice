
""" in *args you can pass as many as arguments which in return
 can be used in form of tuple inside the function """
def func_args(*args):
    print(args)
    print(type(args))
    
    for i in args:
        print(i)
    
    
func_args(10,20,30,40,50,60,70,80,90,100)


""" in **kwargs you can pass as many as
arguments you want in return it can be used in form of dictionary inside function """
def func_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
    for key,value in kwargs.items():
        print(key)
        print(value)
 
func_kwargs(one=1,two=2,three=3)


#combined args