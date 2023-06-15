import logging

def sort_merge(L, R):
"""Here a list of length 1 or 2 is input"""
# order the lists
    if L[0] > L[1]:
        L[1],L[0] = L[0],L[1]
    if R[0] > R[1]:
        R[0],R[1] = R[1],R[0]
# merge by popping the smallest item between the top of the two lists
    M = []
    if L[0] < R[0]:


def recurSplit_compare_merge(list):
    l = len(list)
    m = int(l / 2)
    L = []  # odd when list is odd
    R = []  # always even
    L, R = list[:m], list[m:]
    if l > 2:
        recurSplit_compare_merge(L)
        recurSplit_compare_merge(R)
    else:
        while (L and R):
            if L[0] > L[1]:
                L[1], L[0] = L[0], L[1]
            if R[0] > R[1]:
                R[0], R[1] = R[1], R[0]
            if L[0] < R[0]:
                M.append(L.pop())
            else:
                M.append(R.pop())

def sort(list):
    return recurSplit_compare_merge(list)

def ask_for_list():
    n = int(input("How long is the list?\n"))
    D = []
    i = 0
    while n:
        item = int(input("Enter the next list item\n"))
        D.append(item)
        n -= 1
    return D

def sort_or_None(args):
    if isinstance(args, list):
        return sort(args)
    else:
        print("Error:args not a list")
        return None

def main(args = None):
    if not args:
        ask = ask_for_list()
        main(ask)
    else:
        sorted = sort_or_None(args)
        if sorted:
            for idx,item in enumerate(sorted):
                print(f"{idx,item}\n")


if __name__ == '__main__':
    main()
