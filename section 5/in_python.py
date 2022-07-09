

def passString(str):
    for i in str.lower():
        if( i in ['a','e','i','o','u']):
            return True
    return False        
    
str1='hello'
print("is there a vowel ::{vo}".format(vo=passString(str1)))