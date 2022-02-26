

# noinspection PyUnusedLocal
# skus = unicode string

from itertools import groupby

from enum import Enum

class Offers(Enum):
    BUY_3A_FOR_130 = 'BUY_3A_FOR_130',
    BUY_2A_FOR_45 = 'BUY_2A_FOR_45',



STOCK_LIST_BY_SKUS = (
        ('A', 50, '3A for 130'),
        ('B', 30, '2B for 45'),
        ('C', 20, None),
        ('D', 15, None)
    )

def get_discount_factor(discount_type):
    if discount_type == Offers.BUY_3A_FOR_130.value:
        # Hard coded for now
        return 3, 30
    
    if discount_type == Offers.BUY_2A_FOR_45.value:
        return 2, 15


def apply_discount_factor(stock_item: STOCK_LIST_BY_SKUS, counter: int):
    discount_factor, discounted_price =  get_discount_factor

    if discount_factor:
        if counter % counter == 0:
            return discounted_price
        else:
            return stock_item[1]
    

def checkout(skus):
    # Sort into seperate lists
    incoming_skus = ["".join(group) for _, group in groupby(sorted(skus))]
    price = 0
    try:
        for stock_item in STOCK_LIST_BY_SKUS:
            for skus in incoming_skus:
                if stock_item[0] == skus[0]:
                    # process logic
                    breakpoint()
                    for index, _ in enumerate(list(skus)):
                        price += apply_discount_factor(stock_item, index)

        breakpoint()
        
        return price

    except Exception as e:
        breakpoint()
        return -1




