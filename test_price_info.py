import price_info as PI

def test_cost_of_fruit():
    fruitname = "orange"
    quantity = 5
    expected = 7
    result = PI.cost_of_fruits(fruitname,quantity)
    assert(result==expected)

def test_total_shopping():
    PI.quantity_list={'apple': 5, 'orange':5, 'watermelon': 2, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
    expected = 46.75 + 6.5
    result = PI.total_cost_shopping()
    assert(result==expected)