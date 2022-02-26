from tabnanny import check
from solutions.CHK import checkout_solution

def test_add_item_to_checkout():
    skus = 'A'
    assert 50 == checkout_solution.checkout(skus)

def test_attempt_to_add_non_existant_item():
    skus = 1
    checkout_solution.checkout(skus)

def test_add_multiple_to_checkout():
    skus = 'A, B, C, D'

    checkout_solution.checkout(skus)

def test_special_offers_buy_2():
    skus = 'B'
    assert 30 == checkout_solution.checkout(skus)
    
    skus = 'B, B'
    assert 50 == checkout_solution.checkout(skus)

def test_special_offers_buy_3():
    skus = 'A'
    assert 50 == checkout_solution.checkout(skus)
    
    skus = 'A, A'
    assert 100 == checkout_solution.checkout(skus)

    skus = 'A, A, A'
    assert 130 == checkout_solution.checkout(skus)


