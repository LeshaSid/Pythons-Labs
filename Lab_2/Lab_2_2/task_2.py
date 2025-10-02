def merge_dicts(dict_a, dict_b):
    for key, value in dict_b.items():
        if key in dict_a and type(dict_a[key]) is type(value) is dict:
            merge_dicts(dict_a[key], value)
        else:
            dict_a[key] = value
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(dict_a)