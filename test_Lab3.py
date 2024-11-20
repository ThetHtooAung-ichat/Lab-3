import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_input_too_long():
    expected = 1
    input_arr = [64,34,25,12,22,11,90,11,22,44,332]
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert(result == expected)

def test_input_empty():
    excepted = 0
    input_arr=[]
    result =Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert(result==excepted)

def test_not_integer():
    expected = 2
    input_arr = [64,34,25,12,33,23.5,22.3]
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert(result==expected)
