def merge_sort(list):
    if len(list) <= 1:
        return list

    m = len(list) // 2
    L = list[:m]
    R = list[m:]

    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L, R)


def merge(L, R):
    merged = []
    L_idx = 0
    R_idx = 0

    while L_idx < len(L) and R_idx < len(R):
        if L[L_idx] <= R[R_idx]:
            merged.append(L[L_idx])
            L_idx += 1
        else:
            merged.append(R[R_idx])
            R_idx += 1

    # Append any remaining elements
    while L_idx < len(L):
        merged.append(L[L_idx])
        L_idx += 1

    while R_idx < len(R):
        merged.append(R[R_idx])
        R_idx += 1

    return merged


print(merge_sort([45,23,52,64,73,42,2,123,32,52,63,32]))