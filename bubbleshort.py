def short(list):
    for a in range(len(list)-1,0,-1):
        for b in range(a):
            if list[b] > list[b+1]:
                temp =  list[b]
                list[b] = list[b+1]
                list[b+1] =temp

list=[12,11,45,67,1,3,66]
short(list)
print(list)