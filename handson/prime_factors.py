def prime_factors(n):

    li = prime(n)
    print(li)
    trun=[]
    ind =0
    for i in li:
        ind +=1
        for j in li[ind:]:
            x = i*j
            if (n%x) == 0:
                trun.append(i)
                trun.append(j)
                return trun
def prime(n1):

    li= [2]
    for n in range(3,n1):
        for i in range(2,n):
            if (n%i == 0):
                break
        else :
            li.append(n)
    return li

n= 14
print(prime_factors(n))

n= 15
print(prime_factors(n))
