def flatten_list(lst):
    i = 0
    while i < len(lst):
        item = lst[i]
        if type(item) is list:
            flattened_sublist = flatten_list(item)
            lst[i:i+1] = flattened_sublist
            i += len(flattened_sublist)
        else:
            i += 1
            
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)