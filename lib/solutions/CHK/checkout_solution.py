

# noinspection PyUnusedLocal
# skus = unicode string

from re import I


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
        if sku in stock_item:
            return 0

        raise Exception("Invalid input")

def eligable_for_offer(offer, count):
    if offer == '3A for 130':
        if count % 3:
            return True
        return False

def checkout(skus):
    price = 0
    skus_to_list = skus.split(',')

    psudo_skus = ['A', 'B', 'A']

    try:
        for sku in skus_to_list:
            for stock_item in STOCK_LIST_BY_SKUS:
                local_stock_count = []
                label = stock_item[0]
                if label == sku:
                    local_stock_count.push(sku)
                    offer = stock_item[3]
                    if offer:
                        if eligable_for_offer(offer, len(local_stock_count)):

                            
                    price += stock_item[1]
        
        return price

    except Exception:
        return -1






