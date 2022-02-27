import pytest
from solutions.CHK import checkout_solution

def test_add_multiple_to_checkout():
    skus = 'ABCD'

    assert 115 == checkout_solution.checkout(skus)

def test_special_offers_buy_2():
    skus = 'B'
    assert 30 == checkout_solution.checkout(skus)
    
    skus = 'BB'
    assert 45 == checkout_solution.checkout(skus)

def test_special_offers_buy_3():
    skus = 'A'
    assert 50 == checkout_solution.checkout(skus)
    
    skus = 'AA'
    assert 100 == checkout_solution.checkout(skus)

    skus = 'AAA'
    assert 130 == checkout_solution.checkout(skus)

    skus = 'AAAAA'
    assert 200 == checkout_solution.checkout(skus)

    skus = 'AAAAAA'
    assert 250 == checkout_solution.checkout(skus)

    skus = 'AAAAAAA'
    assert 300 == checkout_solution.checkout(skus)

    skus = 'AAAAAAAA'
    assert 330 == checkout_solution.checkout(skus)

    skus = 'AAAAAAAAA'
    assert 380 == checkout_solution.checkout(skus)

    skus = 'AAAAAAAAAA'
    assert 400 == checkout_solution.checkout(skus)

def test_multiple_product_discounts():
    skus = 'AAABBAAA'

    assert 295 == checkout_solution.checkout(skus)

def test_catch_invalid_input():
    assert -1 == checkout_solution.checkout("1234")
    assert -1 == checkout_solution.checkout("ABCa")
    assert -1 == checkout_solution.checkout("AxA")

def test_summing_new_product():
    skus = 'AAAAAAEEEE'

    assert 410 == checkout_solution.checkout(skus)

def test_shared_discount_applied_for_E_product():
    skus = 'AAAAAABBEE'

    assert 345 == checkout_solution.checkout(skus)
