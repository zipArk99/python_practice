str1 = 'helloWorldHowAreYou'

# printing string characters uptill 5th index
# from : uptill : steps
print(str1[:5])

# printing string characters after 5th index
print(str1[5:])

# printing string characters between 5 to 10 index
print(str1[5:10])


""" #Reverse String 
print(str1[:-1]) """

str2 = ""
for i in str1:
    str2 = i+str2
    print(str2)

print(str2)


name = 'Shaurya'
print(name.split('u'))
name = 'Shaurya '+'Kajiwala'
print(name)




