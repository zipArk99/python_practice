def myfunc(str1):
    str2=''
    for num in range(0,len(str1)):
        if(num%2==0):
            str2+=str1[num].upper()
        else:
            str2+=str1[num].lower()
    return str2
     


print(myfunc('sHaAIipJiHiHijjJ'))