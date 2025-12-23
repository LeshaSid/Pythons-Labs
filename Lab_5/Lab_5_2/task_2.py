def find_unique(ls):
    unique_ls = []
    for n in ls:
        if ls.count(n) == 1:
            unique_ls.append(n)
    return unique_ls

def test_find_unique_basic():
    assert find_unique([1, 2, 2, 3, 4, 4]) == [1, 3]

def test_find_unique_all_unique():
    assert find_unique([1, 2, 3]) == [1, 2, 3]

def test_find_unique_no_unique():
    assert find_unique([1, 1, 2, 2, 3, 3]) == []

def test_find_unique_empty():
    assert find_unique([]) == []

def test_find_unique_strings():
    assert find_unique(["apple", "banana", "apple", "orange"]) == ["banana", "orange"]

def test_find_unique_mixed():
    assert find_unique([1, "a", 1, "b"]) == ["a", "b"]