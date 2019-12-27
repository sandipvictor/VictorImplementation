pos = -1
class search:
    def __init__(self, list, num):
        self.item_list = list
        self.serch_item = num

    def binary_search(self):
        sort_list = sorted(self.item_list)
        lower_bound = 0
        upper_bound = len(list) - 1
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if sort_list[mid] == num:
                globals()['pos'] = mid
                return True
            else:
                if sort_list[mid] < num:
                    lower_bound = mid + 1
                else:
                    upper_bound = mid - 1
        return False


num = int(input("enter the number to be search from list"))
list = [10, 11, 12, 43, 50, 65, 8, 9]
src = search(list, num)
if src.binary_search():
    print("number found at", pos)
else:
    print("number not found")
