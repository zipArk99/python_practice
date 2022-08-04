
class A():
    def __init__(self):
        self.attrA='A class constructor called'
        print(self.attrA)
    def metA(self):
        print('A class method called')

class B(A):
    
    """ def __init__(self):
        self.attrB='B class constructor called'
        print(self.attrB) """
    def metB(self):
        print('B class method called')
        

bobj=B()
bobj.metA()

        


    