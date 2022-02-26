

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
    if discount_type == 

        
    

def checkout(skus):
    # Sort into seperate lists
    incoming_skus = ["".join(group) for _, group in groupby(sorted(skus))]
    try:

        for stock_item in STOCK_LIST_BY_SKUS:
            for skus in incoming_skus:
                if stock_item[0] == skus[0]:
                    # process logic

        breakpoint()
        
        return price

    except Exception as e:
        breakpoint()
        return -1


