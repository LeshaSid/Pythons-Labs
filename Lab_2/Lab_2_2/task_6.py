def flatten_list(lst):
    i = 0
    while i < len(lst):
        item = lst[i]
        if type(item) is list:
            flatten_list(item)
            lst[i:i+1] = item
        else:
            i += 1
            
def unique_elements(a):
        flatten_list(a)
        unique_el = []
        for i in a:
            if i not in unique_el:
                unique_el.append(i)
        return unique_el
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
print(unique_elements(list_a))