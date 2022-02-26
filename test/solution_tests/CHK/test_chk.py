from solutions.CHK import checkout_solution

def test_add_item_to_checkout():
    item = 'A'
    checkout_solution.checkout(item)

def test_attempt_to_add_non_existant_item():
    item = 1
    checkout_solution.checkout(item)

def test_remove_item_added_to_cart()
