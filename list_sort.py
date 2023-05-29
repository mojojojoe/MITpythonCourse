# noinspection PyStatementEffect
def find_max(_list):
    max = 0
    i = 0
    while _list[i]:
        if _list[i] > max:
            max = _list[i]
            _list[i] = -1
        i += 1
    return max

def collect_list():
    _list = []
    j = 1
    while j < 6:
        _list.append(int(input("number?")))
        j += 1
    return _list

def sort(list):
    sorted = []
    while list:
       sorted.append(find_max(list))
    return sorted

def __main__():
    sort(collect_list())

if __name__ == '__main__':
    __main__()