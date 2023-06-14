


def recursplit_compare_merge(list):
    l = len(list)
    if l % 2 == 1:
        print("odd")
    else:
        m = l/2
        L, R = list[:m], list[m:]
    return list

def sort(list):
    return recursplit_compare_merge(list)

def ask_for_list():
    n = int(input("How long is the list?\n"))
    D = []
    i = 0
    while n:
        item = int(input("Enter the next list item\n"))
        D.append(item)
        n -= 1
    return D

def sort_or_break(args):
    if isinstance(args, list):
        return sort(args)
    else:
        print("Error:args not a list")
        return 0

def main(args = None):
    if not args:
        ask = ask_for_list()
        main(ask)
    else:
        sorted = sort_or_break(args)
        if sorted:
            for idx,item in enumerate(sorted):
                print(f"{idx,item}\n")


if __name__ == '__main__':
    main()