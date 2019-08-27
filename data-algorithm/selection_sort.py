def select(a):
    print("array : ",a)
    for i in range(len(a)):
        value = i
        for j in range(i+1,len(a)):
            if a[value] > a[j]:
                value = j
        a[value],a[i] = a[i],a[value]
    return a
select([4,2,1,3])
