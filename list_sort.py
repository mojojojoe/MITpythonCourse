
def  get_max(lst):
    i = 0
    max = 0
    while i < len(lst):
        if lst[i] > max:
            max = lst[i]
            print(max)
            lst[i] = -1
        i = i + 1
        print(max)
        return max

def sort():
    j = 1
    _list_ = []
    while j < 6:
        _list_.append(int(input("number?")))
        j = j + 1
    print(_list_)
    print(len(_list_))
    k = 1
    sorted = []
    while k < len(_list_) + 1:
        sorted.append(get_max(_list_))
        k = k + 1
    return sorted

def __main__():
    print(sort())

if __name__ == '__main__':
    __main__()