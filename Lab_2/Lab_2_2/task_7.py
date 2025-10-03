def merge_sorted_list(list1, list2):
    merged_list = []
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

list1 = [1, 3, 5, 7, 9]
list2 = [0, 2, 4, 6, 8]
print(merge_sorted_list(list1, list2))

list1 = [0, 0, 0, 0, 0]
list2 = [1, 1, 1, 1, 1]
print(merge_sorted_list(list1, list2))