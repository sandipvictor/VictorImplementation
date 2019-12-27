def selection_short(list):

    for a in range(len(list)-1):
        minpos = a
        for b in range(a,7):
            if list[b] < list[minpos]:
                minpos = b
        temp = list[a]
        list[a] = list[minpos]
        list[minpos] = temp



# srch_item= int(input("enter the number for search"))
lst = [12,34,8,9,10,56,6]
selection_short(lst)
print(lst)