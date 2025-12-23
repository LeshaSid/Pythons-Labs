import copy

def combine_dicts(dict_a, dict_b):
    result = copy.deepcopy(dict_a)
    
    for key, value in dict_b.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = combine_dicts(result[key], value)
            elif isinstance(result[key], list) and isinstance(value, list):
                result[key].extend(value)
            elif isinstance(result[key], set) and isinstance(value, set):
                result[key].update(value)
            elif isinstance(result[key], tuple) and isinstance(value, tuple):
                result[key] = result[key] + value
            else:
                result[key] = value
        else:
            result[key] = value
            
    return result


def test_combine_simple():
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3}
    assert combine_dicts(d1, d2) == {'a': 1, 'b': 2, 'c': 3}

def test_combine_lists():
    d1 = {'list': [1, 2]}
    d2 = {'list': [3, 4]}
    assert combine_dicts(d1, d2) == {'list': [1, 2, 3, 4]}

def test_combine_nested_dicts():
    d1 = {'user': {'name': 'Lesha'}}
    d2 = {'user': {'age': 19}}
    expected = {'user': {'name': 'Lesha', 'age': 19}}
    assert combine_dicts(d1, d2) == expected

def test_combine_overwrite():
    d1 = {'status': 'off'}
    d2 = {'status': 'on'}
    assert combine_dicts(d1, d2) == {'status': 'on'}

def test_original_not_changed():
    d1 = {'a': [1]}
    d2 = {'a': [2]}
    combine_dicts(d1, d2)
    assert d1 == {'a': [1]}