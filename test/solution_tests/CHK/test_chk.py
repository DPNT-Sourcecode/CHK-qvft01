from solutions.CHK import checkout_solution

def test_add_item_to_checkout():
    skus = 'A'
    checkout_solution.checkout(skus)

def test_attempt_to_add_non_existant_item():
    skus = 1
    checkout_solution.checkout(skus)

def test_add_multiple_to_checkout():
    skus = 'A, B, C, D'

    checkout_solution.checkout(skus)

def test_special_offers_on_item():
    
    skus = 'A, B, C, D'

