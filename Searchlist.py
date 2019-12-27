
def search(lst,num):
    rng = len(lst)
    for i in range(rng):

        if lst[i] == num:
            print(lst[i])
            return True

sr_item = int(input("enter the number for search in the list"))
list = [12,34,11,32,10,9]

if search(list,sr_item):
    print("number found")
else:
    print("number not found")

