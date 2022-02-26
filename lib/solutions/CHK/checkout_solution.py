

# noinspection PyUnusedLocal
# skus = unicode string

from itertools import groupby

from enum import Enum

class Offers(Enum):
    BUY_3A_FOR_130 = '3A for 130',
    BUY_2A_FOR_45 = '2B for 45',



STOCK_LIST_BY_SKUS = (
        ('A', 50, '3A for 130'),
        ('B', 30, '2B for 45'),
        ('C', 20, None),
        ('D', 15, None)
    )

def get_discount_factor(discount_type: str):
    if discount_type == Offers.BUY_3A_FOR_130.value[0]:
        # Hard coded for now
        return 3, 30
    
    if discount_type == Offers.BUY_2A_FOR_45.value[0]:
        return 2, 15

    return None, 0


def apply_discount_factor(stock_item: STOCK_LIST_BY_SKUS, index: int):
    discount_factor, discounted_price = get_discount_factor(stock_item[2])
    counter = index + 1

    if discount_factor:
        if counter % discount_factor == 0:
            return discounted_price
        else:
            return stock_item[1]
    else:
        return stock_item[1]

def validate_input(skus):
    for sku in skus:
        for _, sku_code in enumerate(list(sku)):
            if sku_code not in ['A', 'B', 'C', 'D']:
                raise Exception("Invalid input detected")
    
    return True









    

def checkout(skus: str):
    """
    Parameters
    ----------

    skus: str
        String containing list of sku's

    
    Returns
    -------

    int
        Returns int price
    """
    incoming_skus = ["".join(group) for _, group in groupby(sorted(skus))]
    price = 0
    try:
        validate_input(incoming_skus)
        for stock_item in STOCK_LIST_BY_SKUS:
            for skus in incoming_skus:
                if stock_item[0] == skus[0]:
                    for index, _ in enumerate(list(skus)):
                        price += apply_discount_factor(stock_item, index)
        
        return price

    except Exception:
        return -1

