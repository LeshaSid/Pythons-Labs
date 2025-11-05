def merge_sorted_ls(ls1, ls2):
    merged_ls = []
    i = 0
    j = 0
    
    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            merged_ls.append(ls1[i])
            i += 1
        else:
            merged_ls.append(ls2[j])
            j += 1
    
    merged_ls.extend(ls1[i:])
    merged_ls.extend(ls2[j:])
    
    return merged_ls

ls1 = [1, 3, 5, 7, 9]
ls2 = [0, 2, 4, 6, 8]
print(merge_sorted_ls(ls1, ls2))

ls1 = [0, 0, 0, 0, 0]
ls2 = [1, 1, 1, 1, 1]
print(merge_sorted_ls(ls1, ls2))