def count_primes(num):
    totalNum=0
    for n1 in range(2,num+1):
        count=0
        for n2 in range(2,n1+1):
            if(n1%n2==0):
                count+=1
            else:
                pass
        if(count<=1):
            totalNum+=1
    return totalNum


print(count_primes(99999))