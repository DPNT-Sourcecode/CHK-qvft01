

# noinspection PyUnusedLocal
# skus = unicode string

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

# STOCK_LIST = [
#     {'sku': 'A', 'price': 50, 'offer': '3A for 130'},
#     {'sku': 'B', 'price': 30, 'offer': '3A for 130'},
#     {'sku': 'C', 'price': 20, 'offer': None},
#     {'sku': 'D', 'price': 15, 'offer': None},

# ]

def validate_item_in_stock(sku):
    for stock_item in STOCK_LIST_BY_SKUS:
        breakpoint()
        if sku in stock_item:
            return 0

        raise Exception("Invalid input")

def apply_offer(offer, count):
    if offer == Offers.BUY_3A_FOR_130.value:
        if count % 3:
            return 130
        return None

    if offer == Offers.BUY_2A_FOR_45.value:
        if count % 2:
            return 45
        return None

def calculate_price(list):
    final_price = 0
    for item in list:
        breakpoint()
        final_price += item.values()

    return final_price
    

def checkout(skus):
    skus_to_list = skus.split(',')

    cart = []
    
    try:
        for sku in skus_to_list:
            for stock_item in STOCK_LIST_BY_SKUS:
                label = stock_item[0]
                if label == sku:
                    cart.append({ sku: stock_item[1] })

        price = calculate_price(cart)
        breakpoint()
        
        return price

    except Exception as e:
        breakpoint()
        return -1

