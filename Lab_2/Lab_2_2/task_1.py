def flatten_list(lst):
    i = 0
    while i < len(lst):
        item = lst[i]
        if type(item) is list:
            flatten_list(item)
            lst[i:i+1] = item
        else:
            i += 1
            
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)