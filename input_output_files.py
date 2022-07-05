myfile1=open('file1.txt')
print(myfile1.read())
myfile1.seek(0)#seek is used to adjust cursor to which ever position you want to bring it.
print(myfile1.read())