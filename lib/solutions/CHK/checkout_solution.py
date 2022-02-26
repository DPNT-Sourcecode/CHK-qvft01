

# noinspection PyUnusedLocal
# skus = unicode string

STOCK_LIST_BY_SKUS = (
        ('A', 50, '3A for 130'),
        ('B', 30, '2B for 45'),
        ('C', 20, None),
        ('D', 15, None)
    )

STOCK_LIST = [
    {'sku': 'A', 'price': 50, }
]
    

def checkout(skus):
    price = 0
    skus_to_list = skus.split(',')

    for sku in skus_to_list:
        for stock_item in STOCK_LIST_BY_SKUS:
            label = stock_item[0]
            if label == sku:
                price += stock_item[1]
            breakpoint()
    raise NotImplementedError()




